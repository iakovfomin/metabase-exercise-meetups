---
name: meetup-followup
description: Turn a raw meetup registration export (CSV or Excel) into a follow-up plan - who to email, in which group, and what each group should hear. Use when someone shares a meetup or event registration file and asks for follow-up, a thank-you plan, segments, or "what do we do with these signups".
---

# Meetup follow-up plan

Input: one registration export with these columns (order does not matter):
`registration_id, name, email, company, job_title, registered_at, attended, referral_source, what_do_you_want_to_learn, how_do_you_analyze_data_today, stayed_for_qa`

Output, written to an output folder:
- `followup_plan.md` - the plan a person reads
- `followup_contacts.csv` - one row per registration, with group, attendance variant and flags, ready for a mail tool

## When invoked as `/meetup-followup` (no arguments)

Do the whole job in one go, without asking the user to confirm between steps.

- **Input:** look in `input/` for `.csv`, `.xlsx` or `.xls` files. Ignore any file in the script's own output format (header starts `group,group_name,attendance,...`). One raw export: use it. Several: use the most recently modified and say which. None: stop and tell the user to put the raw export in `input/`.
- **Output folder:** `output/`.
- **Script:** run it as `python3 .claude/skills/meetup-followup/scripts/followup.py` from the project root; read references from `.claude/skills/meetup-followup/references/`.
- Never edit files in `input/`. In the final summary, name the input file used.

The script does everything that is a count or a rule. You do two things only: label free-text answers, and write one hook per group. Never count, dedupe or assign groups yourself, and never edit numbers in the plan.

## Steps

1. **Prepare.** `python3 scripts/followup.py prepare <file> --out <outdir>`
   If it stops on a missing column, stop and ask the user. Do not guess a mapping.

2. **Label new answers.** Open `<outdir>/answers_to_classify.json`. It lists each distinct "what do you want to learn" answer that is not already in `references/known_answers.json`. Give each one exactly one theme from the table below and write them to `<outdir>/judgment.json`:
   ```json
   {"themes": {"<answer exactly as written>": "<theme>"}}
   ```
   Label by what the person wants, in any language. If an answer fits two themes, take the one higher in the table. If you are not sure, use `none` and say so in `notes`. An empty list means there is nothing to label.

   | Theme | Means | Examples |
   |---|---|---|
   | `evaluating` | Choosing, buying or replacing a BI tool | replacing Looker, justifying a purchase, open source vs cloud |
   | `embedding` | Showing dashboards to their own customers or inside their own app | embedding, sharing with clients |
   | `self_serve` | Getting other people to use data without the data team in the middle | ad hoc request overload, getting execs to look, off spreadsheets, scheduled reports |
   | `craft` | Hands-on practitioner questions | modeling, performance, permissions, version control, naming, data quality |
   | `getting_started` | New to Metabase or to analytics | total beginner, see what it can do, learn SQL |
   | `none` | No goal given | just curious, networking |

   If `prepare` printed unrecognised tool answers, add `"tools": {"<answer>": "<category>"}` using one of: `metabase, looker, tableau, power_bi, other_bi, spreadsheets, code, no_self_serve`.

3. **Build.** `python3 scripts/followup.py build --out <outdir>`
   It prints the group sizes and tells you which hooks are missing.

4. **Write hooks.** Read each group's "What they asked for" line in `followup_plan.md`. Add to `judgment.json`:
   - `"hooks": {"<group key>": "<one or two sentences>"}` for `evaluating, embedding, metabase_users, self_serve, craft, getting_started`. A hook says what to lead with this month, based only on that group's answers.
   - `"notes": ["..."]` for anything a person should know before sending: answers in another language, answers you labelled `none` because you were unsure, anything odd in the file. Up to four. Take any number you quote from the script's output.

   Run step 3 again. Repeat until it prints no missing hooks.

5. **Check, then hand over.** Read the finished plan once. Confirm the "to email" and "held" counts add up to the registration count, and that no hook promises something the template does not. Give the user both files and a three-line summary: how many to email, how many held, who gets a personal note.

## Rules

- Do not invent links, dates, speaker names or product claims. The templates carry `[PLACEHOLDERS]`; leave them for the sender.
- Do not rewrite the email templates. They live in `references/messages.md` so the voice stays the same every month. If the user wants different copy, edit that file.
- Do not send anything. The plan is for a person to review.
- Do not merge or drop people the script kept, and do not rescue people it held. Report disagreements in `notes`.

## How grouping works (for answering questions about the plan)

Each sendable person lands in the first group they match:
1. Evaluating or switching - theme `evaluating`, except student and teacher titles. Personal note from a named sender.
2. Embedding and sharing with customers - theme `embedding`.
3. Already on Metabase - current tool is Metabase, unless they call themselves a beginner.
4. Self-serve and adoption - theme `self_serve`.
5. Modeling, governance and performance - theme `craft`.
6. Getting started - theme `getting_started`.
7. General thank-you - everyone else.

Attendance (`attended`, `no_show`, `unknown`) only changes the opening line. A blank is `unknown`, never a no. People who stayed for Q&A are sorted first within each group.

One email per address. When several names share an address, the person whose name matches the address keeps it and the others are held for review. Same name on two addresses is flagged, not merged.

## Files

- `scripts/followup.py` - cleaning, dedupe, grouping, plan and CSV writer
- `references/messages.md` - email template and brief per group, plus the three opening lines
- `references/known_answers.json` - answers already labelled and reviewed by a person. Add reviewed labels here after each run so the same answer gets the same theme next month.
