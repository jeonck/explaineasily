# CTI (Cyber Threat Intelligence), Explained Simply

> Korean version: [cti-ko.md](./cti-ko.md)

## In One Sentence

**CTI is finding out who is coming after you and how, then changing your defenses to match.**

The second half is what matters. If you learn something and your defenses stay the same, that is not intelligence. That is news.

## What It Feels Like — A Weather Forecast

CTI works like a **weather forecast**.

A weather service collects satellite images, station readings, and historical records. Analysts turn that into "rain in Seoul tomorrow afternoon." You hear it and take an umbrella. CTI has the same shape: collect traces of attacks from many places, analyze them, report that "ransomware aimed at domestic manufacturers is rising this month," and the security team adjusts its backup policy in response.

**But the analogy breaks in one place.** The weather arrives whether or not you carry an umbrella. An attacker does not. When you block them, they change their method. So CTI is not a forecast you produce once — it is a forecast you keep rewriting, because the thing you are forecasting is watching how you respond.

## Why You Need It

Without CTI, a security team runs into three problems.

**1. Every attack looks brand new.**
Another company hit the same way three months ago and published exactly how they handled it. If you do not know that, you start over from zero.

**2. Too many alerts, no way to rank them.**
Security tools generate thousands of alerts a day. Nobody reads them all. CTI adds context — "this IP belongs to a group that is active right now" — so the ten alerts worth opening first rise out of the thousands.

**3. The budget goes to the wrong place.**
If most attacks against your industry arrive by email, and your spending is entirely elsewhere, you are paying for the wrong defense.

## Four Kinds of CTI

The same intelligence looks completely different depending on **who reads it**. Confuse these and you end up handing an executive a list of IP addresses.

| Kind | Reader | Question it answers | Form | Shelf life |
|---|---|---|---|---|
| **Strategic** | Executives, CISO | "What risk are we accepting?" | Reports, trend analysis | Months to years |
| **Operational** | Security leads | "Who is targeting us, and why?" | Campaign analysis | Weeks to months |
| **Tactical** | Analysts, detection engineers | "How do they get in?" | TTP write-ups | Months to years |
| **Technical** | Security tooling | "What do we block?" | IP, hash, domain lists | Hours to days |

Notice that the bottom row **expires fastest**. A list of bad IP addresses is worthless within days, because swapping servers costs the attacker almost nothing.

## Five Terms Worth Knowing

These acronyms are where most people stall. Plain meaning first, original term in parentheses — you need the original to search later.

- **Indicator of Compromise (IOC)** — a piece of evidence that you were already hit. A malicious file's fingerprint (hash), an attacker's server IP, a suspicious domain name.
- **Tactics, Techniques, and Procedures (TTP)** — the attacker's *way of working*. A pattern like "arrives by phishing email, borrows legitimate admin tools, exfiltrates data early on weekend mornings."
- **MITRE ATT&CK** — a free, public catalog of attack techniques observed in the real world. It gives security teams everywhere a shared vocabulary for naming the same behavior.
- **STIX / TAXII** — a format for writing threat information so machines can read it (STIX), and a channel for exchanging it (TAXII). These exist so that people stop trading spreadsheets.
- **Traffic Light Protocol (TLP)** — a color code for how far you may pass information along. CLEAR (public) → GREEN (community) → AMBER (your organization) → RED (recipients only), narrowing at each step.

## One Concrete Example — Blocking an IP vs. Blocking a Method

Say a CTI feed hands you one attacker server IP.

**Option A: block that IP at the firewall.**
Five minutes of work. The attacker rents a new server — a few dollars, ten minutes. You are back where you started.

**Option B: look at *how* that IP was used.**
Analysis shows a pattern: a legitimate remote-admin tool gets installed, then large outbound transfers happen only between 2 and 4 a.m. You turn that **behavior** into a detection rule. Now the attacker can change IPs a hundred times and still trip it. To evade you, they have to redesign how they operate — and that takes months.

This difference is the **Pyramid of Pain**. Lower levels are easy to block and painless for the attacker. Higher levels are hard to block and genuinely painful.

| Top ↑ hard to block | What it costs the attacker to change |
|---|---|
| **TTPs** | Months — they must redesign how they operate |
| **Tools** | Weeks — they must build or learn a new one |
| **Host/network artifacts** | Days — they must change configuration |
| **Domain names** | Hours — they buy another one |
| **IP addresses** | Ten minutes — they rent another server |
| **File hashes** | One second — adding a single byte changes it |
| Bottom ↓ easy to block | |

Most organizations work only the bottom two rows and call it a CTI program. That is usually why it does not feel like it is working.

## How Data Becomes Intelligence

Raw data is not intelligence. It has to pass through six steps.

1. **Direction** — decide what you need to know before collecting anything. (Skipping this is the most common failure.)
2. **Collection** — gather from feeds, dark web sources, internal logs, and industry sharing groups (ISACs).
3. **Processing** — normalize formats, remove duplicates, translate.
4. **Analysis** — attach the "so what does this mean for us?" **This is the step where data becomes intelligence.**
5. **Dissemination** — deliver it in the reader's language. (See the four-kinds table again.)
6. **Feedback** — ask whether it actually helped, then return to step 1.

## Three Common Ways This Fails

- **Subscribing to feeds and never using them.** Nobody reads a feed that delivers 100,000 indicators a day. Volume collected is not a result.
- **Chasing threats that do not apply to you.** A widely reported attack may have nothing to do with your industry or your technology stack. "Does this reach us?" should be question one.
- **Skipping step 1.** Collect without knowing what you are protecting, and you produce reports nobody opens.

## Where to Go Next

Search these terms. In this order, they build on each other.

- `MITRE ATT&CK` — the technique catalog. The fastest place to start.
- `Pyramid of Pain` — the original write-up of the pyramid above (David Bianco, 2013)
- `Diamond Model of Intrusion Analysis` — breaks an intrusion into adversary, capability, infrastructure, and victim
- `Cyber Kill Chain` — models an attack as stages from initial access to objective
- `STIX 2.1`, `TAXII 2.1` — current versions of the exchange standards
- `ISAC`, `TLP 2.0` — sharing communities and distribution markings
