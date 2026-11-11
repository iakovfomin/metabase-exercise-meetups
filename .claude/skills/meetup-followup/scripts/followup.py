#!/usr/bin/env python3
"""Meetup follow-up: deterministic half of the skill.

  followup.py prepare <registrations.csv|.xlsx> --out DIR
  followup.py build --out DIR

prepare  cleans the file, resolves shared email addresses, and lists the
         free-text answers that still need a theme (answers_to_classify.json).
build    reads DIR/judgment.json (themes, hooks, notes written by Claude),
         puts every registrant in exactly one group, and writes
         followup_plan.md + followup_contacts.csv.

Everything that is a count, a join or a rule lives here so it is the same
every month. The model only labels free text and writes one hook per group.
"""
import argparse, csv, json, re, sys, unicodedata
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
COLUMNS = ["registration_id", "name", "email", "company", "job_title", "registered_at",
           "attended", "referral_source", "what_do_you_want_to_learn",
           "how_do_you_analyze_data_today", "stayed_for_qa"]

THEMES = ["evaluating", "embedding", "self_serve", "craft", "getting_started", "none"]

# Group order is priority order: the first rule a person matches wins.
GROUPS = [
    ("evaluating",      "Evaluating or switching"),
    ("embedding",       "Embedding and sharing with customers"),
    ("metabase_users",  "Already on Metabase"),
    ("self_serve",      "Self-serve and adoption"),
    ("craft",           "Modeling, governance and performance"),
    ("getting_started", "Getting started"),
    ("general",         "General thank-you"),
]
GROUP_NAME = dict(GROUPS)

YES = {"yes", "y", "true", "1", "x", "attended"}
NO = {"no", "n", "false", "0"}
FREE_MAIL = {"gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "proton.me",
             "protonmail.com", "icloud.com", "live.com", "aol.com", "me.com"}
NO_COMPANY = {"", "n/a", "na", "none", "-", "self-employed", "self employed", "freelance",
              "freelancer", "independent"}
ACADEMIC = re.compile(r"\b(student|teacher|professor|lecturer|research assistant|intern)\b", re.I)

# First match wins, so combined answers ("dbt + Looker") land on the BI tool.
TOOL_RULES = [
    ("metabase",     r"metabase"),
    ("looker",       r"looker"),
    ("tableau",      r"tableau"),
    ("power_bi",     r"power\s*bi"),
    ("other_bi",     r"superset|redash|mode|sigma|qlik|domo|hex|lightdash|grafana|quicksight"),
    ("spreadsheets", r"excel|sheet"),
    ("code",         r"python|pandas|jupyter|notebook|sql|\br\b|dbt"),
    ("no_self_serve", r"data team|engineers|i don'?t|nothing|not really|no tool"),
]
TOOL_LABEL = {"metabase": "Metabase", "looker": "Looker", "tableau": "Tableau",
              "power_bi": "Power BI", "other_bi": "another BI tool", "spreadsheets": "spreadsheets",
              "code": "code and notebooks", "no_self_serve": "no self-serve tool",
              "unknown": "not stated", "unrecognised": "unrecognised answer"}


def clean(v):
    if v is None:
        return ""
    return re.sub(r"\s+", " ", str(v)).strip()


def key(v):
    return unicodedata.normalize("NFKC", clean(v)).casefold()


def load(path):
    path = Path(path)
    if path.suffix.lower() in (".xlsx", ".xlsm"):
        try:
            import openpyxl
        except ImportError:
            sys.exit("openpyxl is needed for Excel files: pip install openpyxl")
        rows = list(openpyxl.load_workbook(path, read_only=True, data_only=True).active.iter_rows(values_only=True))
    else:
        with open(path, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.reader(f))
    rows = [r for r in rows if r and any(clean(c) for c in r)]
    if not rows:
        sys.exit("The file is empty.")
    header = [key(h).replace(" ", "_") for h in rows[0]]
    missing = [c for c in COLUMNS if c not in header]
    if missing:
        sys.exit(f"Missing expected column(s): {', '.join(missing)}. Found: {', '.join(header)}. "
                 "Stop and ask the user; do not guess a column mapping.")
    return [dict(zip(header, list(r) + [None] * (len(header) - len(r)))) for r in rows[1:]]


def tri(v):
    k = key(v)
    return "yes" if k in YES else "no" if k in NO else "unknown"


def tool_category(v):
    k = key(v)
    if not k:
        return "unknown"
    for cat, pat in TOOL_RULES:
        if re.search(pat, k):
            return cat
    return "unrecognised"


def fmt_date(v):
    if isinstance(v, (datetime, date)):
        return v.strftime("%Y-%m-%d")
    return clean(v)


def fmt_id(v):
    s = clean(v)
    return s[:-2] if re.fullmatch(r"\d+\.0", s) else s


def recase(name):
    """Fix shouting and all-lowercase names; leave mixed case (McKay, de la Cruz) alone."""
    if name and (name == name.upper() or name == name.lower()):
        return " ".join(p.capitalize() for p in name.split(" "))
    return name


def name_tokens(name):
    return [t for t in re.split(r"[^\w]+", key(name)) if t]


def owns(name, email):
    """True when the address looks like it was made from this person's name."""
    local = re.split(r"[^\w]+", key(email).split("@")[0])
    toks = name_tokens(name)
    return bool(toks) and all(t in local for t in toks)


def prepare(args):
    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    raw = load(args.file)
    rows = []
    for r in raw:
        email = key(r["email"])
        name = clean(r["name"])
        domain = email.split("@")[-1] if "@" in email else ""
        company = clean(r["company"])
        first = name.split(" ")[0] if name else ""
        row = {
            "registration_id": fmt_id(r["registration_id"]),
            "name": recase(name),
            "first_name": recase(first),
            "email": email,
            "company": "" if key(company) in NO_COMPANY else company,
            "job_title": clean(r["job_title"]),
            "registered_at": fmt_date(r["registered_at"]),
            "attended": tri(r["attended"]),
            "stayed_for_qa": tri(r["stayed_for_qa"]),
            "learn": clean(r["what_do_you_want_to_learn"]),
            "tool_raw": clean(r["how_do_you_analyze_data_today"]),
            "tool": tool_category(r["how_do_you_analyze_data_today"]),
            "flags": [], "hold": "",
        }
        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
            row["hold"] = "No valid email address"
        elif not email.isascii():
            row["flags"].append("non_ascii_email")
        if row["learn"] and not row["learn"].isascii() and re.search(r"[^\x00-ɏ]", row["learn"]):
            row["flags"].append("non_english_answer")
        if ACADEMIC.search(row["job_title"]):
            row["flags"].append("academic")
        row["_mismatch"] = None
        if domain and domain not in FREE_MAIL and row["company"]:
            first_word = re.sub(r"[^a-z0-9]", "", key(row["company"]).split(" ")[0])
            row["_mismatch"] = bool(first_word) and first_word not in re.sub(r"[^a-z0-9]", "", domain)
        rows.append(row)

    # One send per address. Decide who, if anyone, the address belongs to.
    by_email = defaultdict(list)
    for r in rows:
        if not r["hold"]:
            by_email[r["email"]].append(r)
    for email, grp in by_email.items():
        if len(grp) == 1:
            continue
        names = {key(g["name"]) for g in grp}
        if len(names) == 1:  # same person registered twice: keep the latest
            keep = max(grp, key=lambda g: (g["registered_at"], g["registration_id"]))
            for g in grp:
                if g is not keep:
                    g["hold"] = f"Duplicate registration of {keep['registration_id']}"
            continue
        owners = [g for g in grp if owns(g["name"], email)]
        if len(owners) == 1:
            owners[0]["flags"].append("address_also_used_by_others")
            for g in grp:
                if g is not owners[0]:
                    g["hold"] = (f"Registered with {owners[0]['name']}'s address "
                                 f"(registration {owners[0]['registration_id']}); no address of their own")
        else:
            for g in grp:
                g["hold"] = "Address shared by several names and none clearly owns it"

    by_name = defaultdict(list)
    for r in rows:
        if r["name"] and len(name_tokens(r["name"])) > 1:
            by_name[key(r["name"])].append(r)
    for grp in by_name.values():
        if len({g["email"] for g in grp}) > 1:
            for g in grp:
                g["flags"].append("same_name_other_email")

    seed = json.loads((HERE / "references" / "known_answers.json").read_text(encoding="utf-8"))
    seed = {key(k): v for k, v in seed.items()}
    counts = Counter(r["learn"] for r in rows if r["learn"])
    todo = [{"answer": a, "count": c} for a, c in counts.most_common() if key(a) not in seed]
    odd_tools = Counter(r["tool_raw"] for r in rows if r["tool"] == "unrecognised")

    checked = [r["_mismatch"] for r in rows if r["_mismatch"] is not None]
    stats = {
        "source_file": Path(args.file).name,
        "rows": len(rows),
        "attended": dict(Counter(r["attended"] for r in rows)),
        "company_domain_checked": len(checked),
        "company_domain_mismatch": sum(checked),
        "unrecognised_tools": dict(odd_tools),
    }
    for r in rows:
        del r["_mismatch"]
    (out / "prepared.json").write_text(json.dumps({"stats": stats, "rows": rows}, ensure_ascii=False, indent=1), encoding="utf-8")
    (out / "answers_to_classify.json").write_text(json.dumps(todo, ensure_ascii=False, indent=1), encoding="utf-8")

    held = sum(1 for r in rows if r["hold"])
    print(f"{len(rows)} registrations read from {stats['source_file']}")
    print(f"attended: {stats['attended']}")
    print(f"{len(rows) - held} sendable, {held} held for review")
    print(f"{len(counts)} distinct learning goals, {len(todo)} not in known_answers.json -> {out/'answers_to_classify.json'}")
    if odd_tools:
        print(f"unrecognised tool answers (add to judgment.json 'tools'): {dict(odd_tools)}")


def parse_messages():
    text = (HERE / "references" / "messages.md").read_text(encoding="utf-8")
    sections = {}
    for block in re.split(r"^## ", text, flags=re.M)[1:]:
        head, _, body = block.partition("\n")
        sections[head.strip()] = body.strip()
    return sections


def assign(row, theme):
    if theme == "evaluating" and "academic" not in row["flags"]:
        return "evaluating"
    if theme == "embedding":
        return "embedding"
    # A Metabase user who calls themselves a beginner needs the beginner email, not "skip the intro".
    if row["tool"] == "metabase" and theme != "getting_started":
        return "metabase_users"
    if theme in ("self_serve", "craft", "getting_started"):
        return theme
    return "general"


def build(args):
    out = Path(args.out)
    data = json.loads((out / "prepared.json").read_text(encoding="utf-8"))
    rows, stats = data["rows"], data["stats"]
    jpath = out / "judgment.json"
    judgment = json.loads(jpath.read_text(encoding="utf-8")) if jpath.exists() else {}
    themes = {key(k): v for k, v in json.loads((HERE / "references" / "known_answers.json").read_text(encoding="utf-8")).items()}
    themes.update({key(k): v for k, v in judgment.get("themes", {}).items()})
    tool_fix = {key(k): v for k, v in judgment.get("tools", {}).items()}
    hooks, notes = judgment.get("hooks", {}), judgment.get("notes", [])

    bad = sorted({v for v in themes.values() if v not in THEMES})
    if bad:
        sys.exit(f"Unknown theme(s) {bad}. Allowed: {THEMES}")
    unmapped = sorted({r["learn"] for r in rows if r["learn"] and key(r["learn"]) not in themes})
    if unmapped:
        sys.exit("These answers have no theme yet. Add them to judgment.json 'themes':\n  " + "\n  ".join(unmapped))

    for r in rows:
        if r["tool"] == "unrecognised" and key(r["tool_raw"]) in tool_fix:
            r["tool"] = tool_fix[key(r["tool_raw"])]
        r["theme"] = themes[key(r["learn"])] if r["learn"] else "none"
        r["group"] = "" if r["hold"] else assign(r, r["theme"])

    send = [r for r in rows if not r["hold"]]
    held = [r for r in rows if r["hold"]]
    assert len(send) + len(held) == len(rows), "rows lost"
    assert len({r["email"] for r in send}) == len(send), "an address would be mailed twice"
    assert sum(1 for r in send if r["group"] in GROUP_NAME) == len(send), "someone has no group"

    fields = ["group", "group_name", "attendance", "stayed_for_qa", "first_name", "name", "email",
              "job_title", "company", "current_tool", "learning_goal", "flags", "registration_id"]
    order = {g: i for i, (g, _) in enumerate(GROUPS)}
    send.sort(key=lambda r: (order[r["group"]], {"yes": 0, "unknown": 1, "no": 2}[r["attended"]],
                             r["stayed_for_qa"] != "yes", r["name"]))
    with open(out / "followup_contacts.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields + ["hold_reason"])
        w.writeheader()
        for r in send + held:
            w.writerow({"group": r["group"] or "HOLD", "group_name": GROUP_NAME.get(r["group"], "Held for review"),
                        "attendance": {"yes": "attended", "no": "no_show", "unknown": "unknown"}[r["attended"]],
                        "stayed_for_qa": r["stayed_for_qa"], "first_name": r["first_name"], "name": r["name"],
                        "email": r["email"], "job_title": r["job_title"], "company": r["company"],
                        "current_tool": TOOL_LABEL[r["tool"]], "learning_goal": r["learn"],
                        "flags": ";".join(r["flags"]), "registration_id": r["registration_id"],
                        "hold_reason": r["hold"]})

    msgs = parse_messages()
    L = []
    A = L.append
    att = Counter(r["attended"] for r in send)
    A(f"# Meetup follow-up plan\n")
    A(f"Source: `{stats['source_file']}` · {stats['rows']} registrations · generated {date.today().isoformat()}\n")
    A("## Summary\n")
    A(f"- **{len(send)} people to email** in {sum(1 for g, _ in GROUPS if any(r['group'] == g for r in send))} groups, one email each. "
      f"{att['yes']} attended, {att['no']} did not, {att['unknown']} have no attendance recorded.")
    A(f"- **{len(held)} registrations held back** because they have no address of their own (details at the end).")
    held_leads = [r for r in held if r["theme"] == "evaluating"]
    if held_leads:
        A(f"- **{len(held_leads)} of the held people gave a buying signal** ("
          + ", ".join(r["name"] for r in held_leads) + "). Worth finding their real address by hand.")
    lead = [r for r in send if r["group"] == "evaluating"]
    A(f"- **{len(lead)} people get a personal note, not a mail merge**: they said they are choosing or replacing a BI tool.")
    qa = sum(1 for r in send if r["stayed_for_qa"] == "yes")
    A(f"- {qa} people stayed for Q&A. They are sorted to the top of each group in the contacts file; write to them first.\n")
    if notes:
        A("### This month\n")
        for n in notes:
            A(f"- {n}")
        A("")
    A("## Groups\n")
    A("| # | Group | People | Attended | No-show | Unknown | Stayed for Q&A |")
    A("|---|---|---|---|---|---|---|")
    for i, (g, name) in enumerate(GROUPS, 1):
        m = [r for r in send if r["group"] == g]
        c = Counter(r["attended"] for r in m)
        A(f"| {i} | {name} | {len(m)} | {c['yes']} | {c['no']} | {c['unknown']} | {sum(1 for r in m if r['stayed_for_qa'] == 'yes')} |")
    A(f"| | **Total** | **{len(send)}** | **{att['yes']}** | **{att['no']}** | **{att['unknown']}** | **{qa}** |\n")
    A("Each person is in exactly one group: the first one they match, top to bottom. "
      "The opening line changes with attendance; the rest of the email is the same for the whole group.\n")
    A("### Opening line by attendance\n")
    A(msgs.get("openers", "") + "\n")

    missing_hooks = []
    for i, (g, name) in enumerate(GROUPS, 1):
        m = [r for r in send if r["group"] == g]
        if not m:
            continue
        A(f"## {i}. {name} ({len(m)})\n")
        asks = Counter(r["learn"] for r in m if r["learn"]).most_common(5)
        if asks:
            A("**What they asked for:** " + "; ".join(f"“{a}” ({c})" for a, c in asks) + "\n")
        tools = Counter(TOOL_LABEL[r["tool"]] for r in m).most_common(4)
        A("**What they use today:** " + ", ".join(f"{t} ({c})" for t, c in tools) + "\n")
        if g == "general":
            hook = hooks.get(g, "")
        else:
            hook = hooks.get(g)
            if not hook:
                missing_hooks.append(g); hook = "_(hook not written yet)_"
        if hook:
            A(f"**This month's hook:** {hook}\n")
        A(msgs.get(g, "_(no template in references/messages.md)_") + "\n")
        if g == "evaluating":
            A("| Name | Email | Title | Uses today | Said | Attended | Q&A |")
            A("|---|---|---|---|---|---|---|")
            for r in m:
                A(f"| {r['name']} | {r['email']} | {r['job_title'] or '-'} | {TOOL_LABEL[r['tool']]} | {r['learn']} | {r['attended']} | {r['stayed_for_qa']} |")
            A("")

    A("## Check before sending\n")
    flagged = [("non_ascii_email", "Address contains non-Latin characters. Many mail tools reject these; confirm it is deliverable or correct it."),
               ("address_also_used_by_others", "Other people registered with this person's address. They get one email; the others are in the held list."),
               ("same_name_other_email", "Same name appears under a different address. May be one person registered twice; send to one."),
               ("non_english_answer", "Answered in another language. Consider replying in it."),
               ("academic", "Student or teacher title. Kept out of the personal-note group.")]
    for flag, why in flagged:
        m = [r for r in send if flag in r["flags"]]
        if m:
            A(f"- **{len(m)} × `{flag}`**: {why}")
            if len(m) <= 12:
                A("  " + ", ".join(f"{r['name']} <{r['email']}>" for r in m))
    A("")
    if stats["company_domain_checked"]:
        pct = round(100 * stats["company_domain_mismatch"] / stats["company_domain_checked"])
        A(f"Company names were not used for grouping: for {stats['company_domain_mismatch']} of "
          f"{stats['company_domain_checked']} work addresses ({pct}%) the company field does not match the email domain.\n")
    A(f"## Held for review ({len(held)})\n")
    if held:
        A("| Registration | Name | Address given | Attended | Said | Why held |")
        A("|---|---|---|---|---|---|")
        for r in sorted(held, key=lambda r: (r["theme"] != "evaluating", r["email"])):
            A(f"| {r['registration_id']} | {r['name']} | {r['email']} | {r['attended']} | {r['learn'] or '-'} | {r['hold']} |")
    else:
        A("Nobody.")
    A("")
    (out / "followup_plan.md").write_text("\n".join(L), encoding="utf-8")

    print(f"{len(rows)} registrations = {len(send)} to email + {len(held)} held")
    for g, name in GROUPS:
        print(f"  {name}: {sum(1 for r in send if r['group'] == g)}")
    print(f"wrote {out/'followup_plan.md'} and {out/'followup_contacts.csv'}")
    if missing_hooks:
        print(f"HOOKS MISSING for: {', '.join(missing_hooks)}. Add them to judgment.json and run build again.")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("prepare"); a.add_argument("file"); a.add_argument("--out", default="followup_out")
    b = sub.add_parser("build"); b.add_argument("--out", default="followup_out")
    args = p.parse_args()
    prepare(args) if args.cmd == "prepare" else build(args)
