# Message templates

One section per group. `followup.py build` copies each section into the plan.
Edit the copy here; do not let it be rewritten each month.
Anything in [SQUARE BRACKETS] must be filled in by a person before sending.
`{first_name}` is filled from the contacts file. `{opener}` is the line below that matches the person's attendance.

## openers

- **attended:** Thanks for coming to the Metabase meetup on [EVENT_DATE].
- **no_show:** Sorry we missed you at the Metabase meetup on [EVENT_DATE]. The recording is here: [RECORDING_LINK].
- **unknown:** Thanks for signing up for the Metabase meetup on [EVENT_DATE]. In case you missed any of it, the recording is here: [RECORDING_LINK].

## evaluating

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

## embedding

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

## metabase_users

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

## self_serve

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

## craft

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

## getting_started

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

## general

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
