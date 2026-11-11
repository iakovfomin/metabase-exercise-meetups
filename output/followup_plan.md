# Meetup follow-up plan

Source: `raw.csv` · 178 registrations · generated 2026-11-11

## Summary

- **165 people to email** in 7 groups, one email each. 89 attended, 67 did not, 9 have no attendance recorded.
- **13 registrations held back** because they have no address of their own (details at the end).
- **2 of the held people gave a buying signal** (Ravi Rivera, Hana Rivera). Worth finding their real address by hand.
- **8 people get a personal note, not a mail merge**: they said they are choosing or replacing a BI tool.
- 19 people stayed for Q&A. They are sorted to the top of each group in the contacts file; write to them first.

### This month

- 8 people wrote their learning goal in Chinese (我想了解嵌入功能, 'I want to learn about embedding'): 6 are in the send list and 2 are held. All are flagged non_english_answer. Consider replying in Chinese.
- 6 registrations (4 to email, 2 held) use addresses starting with the Cyrillic 'колин' while the surnames are Latin, which looks like 'Colin' was transliterated or mangled at export. Check these addresses before sending.
- Marcus Mwangi was held at колин.mensah@yahoo.com (registration 41026), but a Marcus Mwangi with his own address (marcus.mwangi@lanternrobotics.com) is in the send list, so he is probably still reached. Ravi Rivera and Hana Rivera, both held, gave buying signals and have no other address.
- The company field mostly does not match the email domain (89 of 96 work addresses), so do not use company names in personalisation.

## Groups

| # | Group | People | Attended | No-show | Unknown | Stayed for Q&A |
|---|---|---|---|---|---|---|
| 1 | Evaluating or switching | 8 | 5 | 3 | 0 | 1 |
| 2 | Embedding and sharing with customers | 20 | 9 | 11 | 0 | 1 |
| 3 | Already on Metabase | 15 | 8 | 5 | 2 | 1 |
| 4 | Self-serve and adoption | 42 | 26 | 14 | 2 | 6 |
| 5 | Modeling, governance and performance | 37 | 23 | 14 | 0 | 8 |
| 6 | Getting started | 24 | 12 | 10 | 2 | 1 |
| 7 | General thank-you | 19 | 6 | 10 | 3 | 1 |
| | **Total** | **165** | **89** | **67** | **9** | **19** |

Each person is in exactly one group: the first one they match, top to bottom. The opening line changes with attendance; the rest of the email is the same for the whole group.

### Opening line by attendance

- **attended:** Thanks for coming to the Metabase meetup on [EVENT_DATE].
- **no_show:** Sorry we missed you at the Metabase meetup on [EVENT_DATE]. The recording is here: [RECORDING_LINK].
- **unknown:** Thanks for signing up for the Metabase meetup on [EVENT_DATE]. In case you missed any of it, the recording is here: [RECORDING_LINK].

## 1. Evaluating or switching (8)

**What they asked for:** “Interested in the open source version vs cloud” (4); “Looking to replace Looker, cost is killing us” (2); “I need to justify a BI purchase to my CFO” (2)

**What they use today:** spreadsheets (3), Metabase (2), Power BI (1), no self-serve tool (1)

**This month's hook:** Lead with cost and the open source vs cloud choice: half of this group asked how the two differ, and the rest are weighing a Looker replacement or building a case for their CFO.

**Who sends it:** a named person, one at a time. Not a mail merge.
**What they should hear:** we read what you wrote, here is the one thing that answers it, and a person will talk to you if you want.
**One ask:** reply, or book 20 minutes.

> Subject: Your question about [THEIR WORDS, e.g. replacing Looker]
>
> Hi {first_name},
>
> {opener}
>
> You wrote that you're [THEIR GOAL IN THEIR WORDS]. [ONE SENTENCE THAT ANSWERS IT, WITH ONE LINK: pricing, open source vs cloud comparison, or a migration story from the tool they use today.]
>
> If it helps, I can do 20 minutes on your setup: [BOOKING_LINK]. Or just reply here.
>
> [SENDER NAME]

| Name | Email | Title | Uses today | Said | Attended | Q&A |
|---|---|---|---|---|---|---|
| Josie Achebe | josie.achebe@kestrelsw.io | Sr. Data Analyst | spreadsheets | Looking to replace Looker, cost is killing us | yes | yes |
| Anders Saito | anders.saito@gmail.com | marketing operations | Power BI | I need to justify a BI purchase to my CFO | yes | no |
| Arjun Osei | arjun.osei@gmail.com | Data Engineer | no self-serve tool | Interested in the open source version vs cloud | yes | unknown |
| Karim Haddad | karim.haddad@northwindlog.com | Consultant | spreadsheets | Interested in the open source version vs cloud | yes | unknown |
| Sam Mbeki | sam.mbeki@gmail.com | Growth Marketer | Metabase | Interested in the open source version vs cloud | yes | unknown |
| Devin Rivera | devin.rivera@verdantag.co | data scientist | spreadsheets | I need to justify a BI purchase to my CFO | no | unknown |
| Hana Castellanos | hana.castellanos@verdantag.co | Finance Analyst | not stated | Looking to replace Looker, cost is killing us | no | unknown |
| Thandi Mwangi | thandi.mwangi@lanternrobotics.com | Senior Data Analyst | Metabase | Interested in the open source version vs cloud | no | unknown |

## 2. Embedding and sharing with customers (20)

**What they asked for:** “sharing dashboards externally with clients” (11); “我想了解嵌入功能” (6); “Embedding dashboards in our own app” (3)

**What they use today:** spreadsheets (5), Metabase (3), another BI tool (3), Looker (3)

**This month's hook:** Lead with sharing dashboards with external clients, which is what most of this group asked about; six of them asked about embedding in Chinese, so consider a reply in that language.

**What they should hear:** embedding and customer-facing dashboards are a supported path, and here is where to start.
**One ask:** look at the embedding starting point.

> Subject: Embedding Metabase in your own product
>
> Hi {first_name},
>
> {opener}
>
> You asked about putting dashboards in front of your own customers. The quickest way to see what that takes is [EMBEDDING_QUICKSTART_LINK].
>
> If you tell me what your app is built in, I'll point you at the closest example.
>
> [SENDER NAME]

## 3. Already on Metabase (15)

**What they asked for:** “performance tuning on big tables” (3); “Our analysts are drowning in ad hoc requests” (2); “self service analytics without me being the bottleneck” (1); “data quality / trust issues - people dont believe the numbers” (1); “How do you handle row level permissions?” (1)

**What they use today:** Metabase (15)

**This month's hook:** Lead with performance on big tables, the most common question here, then the ad hoc request load and row-level permissions as the next topics for existing users.

**What they should hear:** you already use Metabase, so no pitch. Here is the deeper material, and we would like to hear how you use it.
**One ask:** share a tip or a talk idea for the next meetup.

> Subject: For people already running Metabase
>
> Hi {first_name},
>
> {opener}
>
> Since you're already on Metabase, I'll skip the intro material. [ONE LINK MATCHED TO THIS MONTH'S HOOK.]
>
> We want more talks from people who run it day to day. If you have five minutes of "here's how we do it", reply and I'll save you a slot on [NEXT_MEETUP_DATE].
>
> [SENDER NAME]

## 4. Self-serve and adoption (42)

**What they asked for:** “How to get execs to actually look at the data” (10); “How to model data for non technical users” (7); “Our analysts are drowning in ad hoc requests” (6); “self service analytics without me being the bottleneck” (5); “Want to automate our weekly reporting” (4)

**What they use today:** another BI tool (11), spreadsheets (8), Tableau (6), no self-serve tool (6)

**This month's hook:** Lead with getting executives and non-technical people to actually use the dashboards that exist, since that and modeling for non-technical users came up most, then the ad hoc request load and automated weekly reports.

**What they should hear:** the problem you described is the bottleneck problem, and other teams have a pattern for getting out of it.
**One ask:** read one how-to.

> Subject: Getting your team their own answers
>
> Hi {first_name},
>
> {opener}
>
> A lot of you described the same thing: too many ad hoc requests and not enough people looking at the dashboards that exist. [SELF_SERVE_GUIDE_LINK] is the pattern most teams start with.
>
> Next meetup is [NEXT_MEETUP_DATE]. Reply with the question you most want covered.
>
> [SENDER NAME]

## 5. Modeling, governance and performance (37)

**What they asked for:** “curious how others structure their models” (8); “troubleshooting slow questions” (6); “performance tuning on big tables” (5); “data quality / trust issues - people dont believe the numbers” (5); “best practices for naming things so people can find them” (5)

**What they use today:** spreadsheets (11), code and notebooks (10), another BI tool (6), no self-serve tool (4)

**This month's hook:** Lead with how others structure their models and with troubleshooting slow questions and big-table performance; data trust and naming conventions are the next most asked.

**What they should hear:** practical answers to the hands-on questions you asked, from people who have done it.
**One ask:** read the one resource for your topic, or bring the question to the forum.

> Subject: Follow-up on the questions you sent in
>
> Hi {first_name},
>
> {opener}
>
> The questions that came up most were about [THE 2-3 TOPICS NAMED IN THIS MONTH'S HOOK]. Best starting point for each: [ONE LINK PER TOPIC].
>
> If yours wasn't answered, post it at [FORUM_LINK] and we'll pick it up.
>
> [SENDER NAME]

## 6. Getting started (24)

**What they asked for:** “Want to see what Metabase can do” (12); “Getting started - total beginner” (7); “I want to learn SQL better” (5)

**What they use today:** code and notebooks (5), Metabase (4), no self-serve tool (4), another BI tool (4)

**This month's hook:** Lead with a hands-on look at what Metabase can do using sample data, since that was the top ask; mention SQL practice for the five who want to learn SQL better.

**What they should hear:** you can try this in an afternoon, and here is the first step.
**One ask:** do the getting-started walkthrough.

> Subject: A first hour with Metabase
>
> Hi {first_name},
>
> {opener}
>
> If you're new to this, start here: [GETTING_STARTED_LINK]. It uses sample data, so you don't need your own database to try it.
>
> Next meetup is [NEXT_MEETUP_DATE].
>
> [SENDER NAME]

## 7. General thank-you (19)

**What they asked for:** “nothing specific, just networking” (3); “just curious” (2)

**What they use today:** no self-serve tool (6), another BI tool (5), Looker (3), spreadsheets (2)

**What they should hear:** thanks, here is the recording, here is the next date. Nothing else.
**One ask:** save the next date.

> Subject: Recording and next date
>
> Hi {first_name},
>
> {opener}
>
> Recording: [RECORDING_LINK]. Next meetup: [NEXT_MEETUP_DATE].
>
> If there's a topic you'd like covered, reply and tell me.
>
> [SENDER NAME]

## Check before sending

- **4 × `non_ascii_email`** (plus 2 in the held list, 6 in total): Address contains non-Latin characters. Many mail tools reject these; confirm it is deliverable or correct it.
  Колин Vance <колин.vance@brightlinehealth.com>, Колин Mensah <колин.mensah@yahoo.com>, Колин Adeyemi <колин.adeyemi@yahoo.com>, Колин Sorensen <колин.sorensen@gmail.com>
- **11 × `address_also_used_by_others`**: Other people registered with this person's address. They get one email; the others are in the held list.
  Колин Mensah <колин.mensah@yahoo.com>, Theo Kaur <theo.kaur@yahoo.com>, Alejandra Lindqvist <alejandra.lindqvist@lanternrobotics.com>, Greta Haddad <greta.haddad@copperline.media>, Owen Rahimi <owen.rahimi@proton.me>, Hana Lombardi <hana.lombardi@verdantag.co>, Chen Barros <chen.barros@proton.me>, Sarah Krishnan <sarah.krishnan@lanternrobotics.com>, Tobi Castro <tobi.castro@yahoo.com>, Rory Moreau <rory.moreau@copperline.media>, Sam Nilsen <sam.nilsen@gmail.com>
- **11 × `same_name_other_email`** (plus 1 in the held list, 12 in total): Same name appears under a different address. May be one person registered twice; send to one.
  Marcus Mwangi <marcus.mwangi@lanternrobotics.com>, Owen Mensah <owen.mensah@brightlinehealth.com>, Theo Kaur <theo.kaur@yahoo.com>, Caleb Castellanos <caleb.castellanos@lanternrobotics.com>, Ibrahim Kaur <ibrahim.kaur@meridianfreight.com>, Caleb Castellanos <caleb.castellanos@brightlinehealth.com>, Theo Oyelaran <theo.oyelaran@northwindlog.com>, Owen Mensah <owen.mensah@verdantag.co>, Theo Kaur <theo.kaur@brightlinehealth.com>, Theo Oyelaran <theo.oyelaran@lanternrobotics.com>, Ibrahim Kaur <ibrahim.kaur@lanternrobotics.com>
- **6 × `non_english_answer`** (plus 2 in the held list, 8 in total): Answered in another language. Consider replying in it.
  Dmitri <dmitri.osei@outlook.com>, Pavel Brennan <pavel.brennan@orchardlabs.dev>, Dara Tanaka <dara.tanaka@gmail.com>, Sarah <sarah.zhou@kestrelsw.io>, Simone Nakamura <simone.nakamura@orchardlabs.dev>, Yuki <yuki.whitlock@northwindlog.com>
- **12 × `academic`** (plus 1 in the held list, 13 in total): Student or teacher title. Kept out of the personal-note group.
  Josie Castellanos <josie.castellanos@northwindlog.com>, Pavel Brennan <pavel.brennan@orchardlabs.dev>, Dara Tanaka <dara.tanaka@gmail.com>, Yuki <yuki.whitlock@northwindlog.com>, Колин Mensah <колин.mensah@yahoo.com>, Owen Mensah <owen.mensah@brightlinehealth.com>, Hugo Rivera <hugo.rivera@meridianfreight.com>, Bea Haddad <bea.haddad@gmail.com>, Ibrahim Kaur <ibrahim.kaur@meridianfreight.com>, Suri Castro <suri.castro@gmail.com>, Chen Novak <chen.novak@verdantag.co>, Tobi Dalgaard <tobi.dalgaard@gmail.com>

Company names were not used for grouping: for 89 of 96 work addresses (93%) the company field does not match the email domain.

## Held for review (13)

| Registration | Name | Address given | Attended | Said | Why held |
|---|---|---|---|---|---|
| 41027 | Ravi Rivera | hana.lombardi@verdantag.co | no | Interested in the open source version vs cloud | Registered with Hana Lombardi's address (registration 41020); no address of their own |
| 41052 | Hana Rivera | owen.rahimi@proton.me | yes | Looking to replace Looker, cost is killing us | Registered with Owen Rahimi's address (registration 41048); no address of their own |
| 41137 | Yuki Rahimi | alejandra.lindqvist@lanternrobotics.com | no | best practices for naming things so people can find them | Registered with Alejandra Lindqvist's address (registration 41090); no address of their own |
| 41046 | Greta Whitlock | chen.barros@proton.me | yes | - | Registered with Chen Barros's address (registration 41009); no address of their own |
| 41074 | Cleo Mensah | greta.haddad@copperline.media | yes | - | Registered with Greta Haddad's address (registration 41040); no address of their own |
| 41131 | Anders Volkov | rory.moreau@copperline.media | yes | 我想了解嵌入功能 | Registered with Rory Moreau's address (registration 41003); no address of their own |
| 41140 | Tom Whitlock | rory.moreau@copperline.media | unknown | How to get my team off spreadsheets | Registered with Rory Moreau's address (registration 41003); no address of their own |
| 41110 | Vik Lindqvist | sam.nilsen@gmail.com | no | nothing specific, just networking | Registered with Sam Nilsen's address (registration 41008); no address of their own |
| 41044 | Omar Olsen | sarah.krishnan@lanternrobotics.com | no | curious how others structure their models | Registered with Sarah Krishnan's address (registration 41025); no address of their own |
| 41154 | Nadia Petrov | theo.kaur@yahoo.com | yes | Our analysts are drowning in ad hoc requests | Registered with Theo Kaur's address (registration 41080); no address of their own |
| 41067 | Jules | tobi.castro@yahoo.com | yes | How to model data for non technical users | Registered with Tobi Castro's address (registration 41032); no address of their own |
| 41026 | Marcus Mwangi | колин.mensah@yahoo.com | yes | Our analysts are drowning in ad hoc requests | Registered with Колин Mensah's address (registration 41021); no address of their own |
| 41156 | Hugo Ferraro | колин.mensah@yahoo.com | no | 我想了解嵌入功能 | Registered with Колин Mensah's address (registration 41021); no address of their own |
