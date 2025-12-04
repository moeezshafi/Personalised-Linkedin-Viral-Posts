from database import SessionLocal, LinkedInPost

db = SessionLocal()

# Clear existing data
db.query(LinkedInPost).delete()

# Training posts
posts = [
    """Startups who work with us don't just launch, they scale. When we first partnered with this startup, they had an idea, a deck, and a deadline. That was it. Here's how we turned their vision into a product used by thousands, and fast:

MVP in 6 Weeks We helped define core features, built lean, and launched a usable product within 45 days.

Scalable Tech Stack We didn't just code, we architected. The foundation was built to handle 10x growth without breaking.

User-Centric Design Product-market fit matters. Our UX team ensured the interface spoke directly to early adopters.

Iterative Development We used weekly sprints + real-time feedback loops to ship fast and pivot faster. 

Within 3 months:
15,000+ active users
38% user retention (industry avg: 20%)
Reduced development cost by 35% compared to internal hires 

Clear code. Clear goals. Clear outcomes. We've worked with 40+ startups at pre-seed to Series A — and helped them raise over $22M combined. 

If you're a founder, what's your biggest fear when building v1? Tech debt? Missed timelines? The wrong team? 

We're not just devs. We're your technical cofounders (without equity). DM me and let's build something that scales. 

Startups we build for raise 2.3x faster than industry average, because they show real traction.""",

    """I know two founders.
One works 100 hours/week. One works 20.

The 20-hour founder makes more.

The 100-hour founder:
-  Raised $50M
-  Burns $1M/month
-  Owns 5%

The 20-hour founder:
-  Raised $0
-  Profits $300K/month
-  Owns 100%

I asked the 20-hour founder his secret.

I only do three things:
1. Build what someone already paid for
2. Charge 10x what feels comfortable
3. Say no to everything else

The 100-hour founder does everything. The 20-hour founder does what matters.

The line that broke me:
"Your investors aren't your friends. They're your landlords. And rent is due every board meeting."

Meanwhile, the bootstrap founder? No landlords. No rent. Just ownership.

Here's the truth:
Working 100 hours means you can't prioritize. 
Raising money means you're in debt. 
Having 200 employees means you're hiding.

Behind one product that works.

The math that matters:
$100M exit at 5% = $5M (maybe) 
$5M exit at 100% = $5M (definitely)

One takes 10 years. One takes 5 years.

Your burn rate isn't your momentum.
It's your countdown clock.

The 100-hour founder is building a prison. 
The 20-hour founder is building a life.

Stop confusing busy with productive. 
Stop confusing funding with success. 
Stop confusing growth with progress.

The best companies aren't the biggest. They're the ones you still own.""",

    """"We have no competitors."

I immediately know you will FAIL.

Here's what "no competition" actually means:

Option 1: The market doesn't exist 
Option 2: You haven't looked hard enough
Option 3: Everyone who tried this failed

None of these are good.

Smart investors know:
- Uber had 15 competitors
- Facebook had MySpace, Friendster
- Shopify competed with Magento, WooCommerce
- Airbnb fought hotels AND Craigslist

Competition validates demand. 

We've built products in "empty" markets:
- Founder: "No one does social media for pets"
- Reality: 47 apps, all with 10 users each
- Outcome: Another app with 10 users

Vs products with clear competition:
- Founder: "We're building a better Slack"
- Reality: $20B market, proven demand
- Outcome: $2M ARR competing on specific features

The uncomfortable pattern:
"No competition" founders: 4% success rate 
"Better than X" founders: 34% success rate

If 10 companies are fighting for the same customers, those customers EXIST and are PAYING. 

If zero companies are in your space, maybe there's a reason. 

Your real homework: 
- Find your 5 closest competitors
- Study why customers choose them
- Then build something 10x better in one specific area""",

    """Every founder defending their over-engineered mess says the same thing:

"I'd rather under-engineer than over-engineer."

Then they build 47 microservices for 100 users.

Here's the DELUSION I keep hearing:
"If there's a 50% chance we'll need this feature, and it only costs 10% more to build it right..."

Stop right there.

You're not assigning probabilities. You're GUESSING.
And your guess is always wrong.

The brutal math of "doing it right": 
That "10% extra effort" compounds into:
- 10% more containerized services to maintain
- 10% more Docker deployment bugs to fix
- 10% more DevOps onboarding complexity
- 10% slower CI/CD pipeline velocity

Multiply that across 50 "might need it" decisions? 
You're now 500% slower than your competitor.

Here's what actually happens: 
CTOs say "We might go international, so let's implement GraphQL with multi-region Redis clusters" then die before leaving the US. 

They declare "We could hit 1M users, better architect event-driven microservices with Apache Kafka" and never break 1,000. 

The "pragmatist" lie:
Every over-engineer calls themselves a pragmatist.

Real pragmatism? Ship garbage that works TODAY.

Your "technical debt" from monolithic architecture with 100 users is irrelevant. 
Your "cloud-native containerized solution" with zero revenue is worthless.

The interest rate on tech debt is NEGATIVE when you're pre-product-market fit.

Because that debt might never come due.

75% of startups die before their tech debt matters.
But 100% of over-engineered startups die before shipping.

Here's the truth that will hurt:
You're not "thinking like a business person" when you calculate engineering ROI.
You're procrastinating with spreadsheets.

Real business thinking: Will this make customers pay us TODAY?
No? Then you're building your resume, not a business.""",

    """If I had $30K to build a software startup today, This is EXACTLY how I'd do it.

Startups rarely fail because of bad code.
They fail after launch — when real users touch it and nobody pays.

That's why my first step wouldn't be writing code.
It would be talking to customers.

I've seen 100s of "perfect" MVPs launch to crickets:
- Zero user interviews
- Features built on assumptions
- Solutions nobody asked for

Here's the test I'd use: 
If 10 people won't pay you $100 to solve their problem, you don't have a business.

If I had to start from zero tomorrow, here's exactly how I'd do it:

01. I'd treat every feature like it's trying to kill my runway.
I'd audit my feature list like I'm looking for budget vampires:
- Does this solve the core problem?
- Will users pay more if this exists?
- Can I validate this without building it?

If it doesn't directly lead to revenue, I kill it. 
Cool features win hackathons. Boring features win customers.

02. I'd build broken before I build beautiful.
I'd start with a raw, functional MVP with zero polish. 
No custom UI. Just forms, tables, and basic workflows.

That version tells the truth. 
I want to see what confuses users, what they ignore, what makes them pay…not after launch, but now.

Beautiful hides problems. Broken reveals them.

03. I'd hire for speed, not prestige.
I'd never hire the ex-Google engineer who wants to build microservices for an MVP.

I'd find the scrappy developer who's shipped 3 startups and thinks "good enough" is a feature, not a bug.

$20K for someone who ships in 7 weeks beats $80K for someone who architects for 6 months.

04. I'd obsess over unit economics like my life depends on it.
Because it kinda does.

If my CAC is higher than 3x LTV before I prove retention, I don't scale it. 
A SaaS that costs $200 to acquire $50/month customers? I'm out.

05. I'd turn early users into my co-founders.
I'd keep my first 10 users looped in like they own equity.

Because building with them is the only way to find product-market fit.

Weekly calls. Usage data. Brutal feedback.

If they churn, I pivot fast. 
If they can't live without it, I double down.

The math that actually works:
$3K: Customer interviews (100 people)
$20K: Scrappy developer (7 weeks)
$7K: Tools + Oh-shit fund (because something will break)

If you want to survive the startup valley of death, you need to be intentional.

Talk first → build fast → iterate faster.

Drop "framework" in the comments if you want the full breakdown.
I'll send you the step-by-step that's saved founders six figures in wasted development."""
]

posts.append("""I just INVENTED the FUTURE of sales calls.
I built a complete MVP on call while the client was explaining his idea.
He couldn't believe what he was watching...

Yesterday, 2:30 PM.
Discovery call with a founder who wants "Tinder for Real Estate."

He starts explaining: "Users swipe on properties, match with co-buyers..."

And I'm thinking: screw this.

Instead of taking notes...
I quietly open bolt.new & superwhisper.

As he talks, Super Whisper transcribes everything in real-time.
I'm copy-pasting his exact words straight into Bolt prompts.

He has NO IDEA what I'm doing.
Still explaining his vision for 30 minutes.

Then he finishes:
"So that's the complete app. Think you can build something like this?"

I hit "Share Screen."

You mean... like this?

His jaw DROPS

Every single feature he just described... WORKING. LIVE. BUILT FROM HIS OWN WORDS.

Complete silence.

Then: "WHAT?! This is EXACTLY what I imagined! How did you just...?!"

But it gets crazier...

He starts swiping frantically.
Testing every feature. Finding co-buyers.

"This already works better than my mental picture!"

I got $15K contract signed before we hung up.

Your prospects don't want to imagine solutions.
They want to see them. Touch them. Test them.

And nothing sells like:
Here. Try it. Right now

P.S. This entire post came from that meeting recording.
Stories like this happen daily but never become content. Pure LinkedIn gold just sitting in your meeting recording.

That's why I'm building Echo - turn conversations into posts. Testing with early users.""")

# Add batch 2 posts
batch2_posts = [
    """Your CTO just spent $3M on microservices.
I'm about to show you why they should be FIRED.

THE $3M ARCHITECTURE MASSACRE:

Ex-Netflix CTO joins a startup.
1,000 users. $5M Series A.

First move? Build 47 microservices.

Your CTO builds for 6 months:
- Kubernetes for 1,000 users
- Event sourcing for events that DON'T EXIST
- $52,000/month infrastructure bill
- 15 engineers just to keep it ALIVE

Meanwhile, companies worth BILLIONS are laughing at you:

Shopify: $230B valuation, MONOLITH 
Stack Overflow: 100M developers, MONOLITH 
GitHub: Sold for $7.5B, MONOLITH

HERE'S THE BRUTAL TRUTH:

Customer asks: "Can you add a wishlist?" 
CTO: "3 months. Need to update 5 services." 
Customer: goes to competitor

Founder fires the CTO.
Hires someone who understands REALITY.

8 WEEKS LATER: 
- All 47 microservices → 1 Rails monolith
- $52,000/month → $800/month
- 15 engineers → 3 engineers
- Wishlist feature → 2 DAYS

THE PATTERN I SEE EVERYWHERE:

Startups with microservices: Dead in 18 months, $3M burned 
Startups with monoliths: $30M ARR, 3 engineers

The difference? 
One built for their résumé. 
One built for customers.

At 500K users, that monolith needed:
- $2K in database upgrades
- That's it

The microservices would've needed:
- $200K/month
- 30 engineers
- A miracle

THE REAL STARTUP PLAYBOOK:
- Ship FAST with boring tech
- Fix problems you ACTUALLY have
- Burn less than your competitor's AWS bill

Amazon Prime Video moved BACK to monoliths. Cut costs by 90%.

But your 1,000-user startup needs distributed architecture?""",

    """The system I wish I had 5 years ago:

I've helped founders build 53+ startups generating $21M+ ARR.

First-time founders always skip step 3. It costs them everything.

STEP 1: Start With Problems, Not Ideas

Most founders: "I have this cool idea for an app..." 
Winning founders: "I found people spending $500/month on a broken solution."

Problem-first thinking changes everything.

Find expensive, frequent, painful problems. Then build the simplest solution.

STEP 2: The Fake Buy Test

Before building anything: 
• Create a simple landing page 
• Add "Buy Now - $49" button 
• When clicked: "Thanks! We'll email you when ready." 
• Drive 100 visitors

10+ people clicked "Buy"? Build it. 
Under 10? Find a new problem.

This saved me from wasting 6 months on products nobody wanted.

STEP 3: Talk to 50 Customers Before Writing Code

Not surveys. Not online research. Actual phone conversations.

Ask: "Walk me through the last time you had this problem." 
Ask: "What did you try to solve it?" 
Ask: "How much did that cost you?"

Real problems become obvious after 20 conversations. 
Fake problems disappear after 5.

STEP 4: MVP in 4 Weeks, Not 4 Months

Your first version should embarrass you. If it doesn't, you waited too long.

Zapier's first MVP: A Google Sheets script
Airtable's first MVP: A simple database 
Notion's first MVP: A basic note-taking app

Perfect is the enemy of launched.

STEP 5: Target 100 Users Who LOVE You

Not 10,000 users who "like" you. 
100 users who can't live without you.

100 users who: 
• Use your product daily 
• Tell their friends about it 
• Would be genuinely upset if it disappeared

These 100 become your growth engine.

Most founders build for everyone. Smart founders build for someone specific.

Most founders launch with 47 features. Smart founders launch with 1 feature that works perfectly.

The goal isn't to impress investors. The goal is to solve real problems for real people.""",

    """I charged a client $20K for an MVP. They made $0.

Their competitor spent $10K but talked to 100 customers.

Guess which one just hit $10k MRR?

CLIENT A (My $20K MVP):
-  3 months of development
-  Perfect UI/UX design
-  Zero customer interviews
-  Launched to crickets
-  Still at $0 revenue

CLIENT B (Their competitor):
-  Spent $1K on: landing page
-  Spent $3k on prototype on lovable for full vision
-  Interviewed 100 potential customers
-  Found 3 critical pain points we missed
-  Pre-sold $10K before building anything
-  Now at $10K MRR and growing

The painful truth?

I helped Client A build the WRONG thing perfectly.
Client B built the RIGHT thing imperfectly.

Here's what Client B did that we didn't:

Week 1-2: Built landing page + lovable prototype (1 core feature) 
Week 3-6: Talked to 25 customers per week 
Week 7-8: Created visual roadmap showing full product vision 
Week 9-12: Pre-sold using prototype + roadmap visualization

Total cost: $10K 
Total validation: Priceless

The power? Customers could SEE and FEEL the future product.

Client A's approach: 
Month 1-3: Built in isolation 
Month 4: Launched to silence 
Month 5-12: Wondering what went wrong

The hardest lesson I learned as a dev shop owner:

Code is cheap. Customer insights are expensive. 
But showing customers their future? That's where the magic happens.

Building without talking to customers is the most expensive mistake of all.

Now we refuse to write a single line of code until clients have talked to at least 10 potential customers.

Some founders hate this rule. The successful ones thank us later.""",

    """Microsoft made $3 TRILLION by shipping garbage for 50 years.

Meanwhile, you spend 18 months perfecting their MVP.

From last 50 years Microsoft:
→ Ship garbage (Windows ME, Vista, Zune) 
→ Let customers complain 
→ Fix it in the next version 
→ Charge them again 
→ Repeat for 50 years 
→ Worth $3 trillion

- Windows crashed daily.
- Internet Explorer was a joke.

But they shipped anyway.
Every. Single. Time.

While you are:
- Adding "just one more feature."
- Obsessing over pixel-perfect designs.
- Waiting for 99.9% uptime.

Here's what Microsoft understood that most founders don't:

Shipping beats perfection

Windows 95 had 5,000 known bugs at launch.
It sold 40 million copies in its first year.

Google shipped Gmail in beta for 5 years.
Facebook's first tagline was "A Mark Zuckerberg production."
Amazon's website looked like it was built in 1997... because it was.

And they kept it that way for YEARS.

The pattern?
Ship fast. Fix later. Dominate markets.

While competitors were still "perfecting" their products.

Your MVP doesn't need to be perfect.
It needs to solve ONE problem better than anything else.

The rest is just expensive procrastination.

Microsoft became the most valuable company on Earth not by building perfect software.

But by consistently shipping imperfect solutions faster than everyone else.

Your startup will die from perfectionism long before it dies from shipping too early.""",

    """I met a guy making $35K/month by COPYING other people's apps.

He was an OPTICIAN 3 years ago.
Taught himself to code in 15 hours watching YouTube.

While every startup guru preaches "find your unique value proposition," Samuel does the exact opposite.

His strategy is brutally simple:

1. Find apps posting MRR screenshots on Twitter
2. Copy their concept with tiny improvements
3. Launch in 2 weeks
4. Steal their customers

The results are undeniable:
-  Story Short AI: $20K/month (copied a YouTube automation tool)
-  Artimus: $15K/month (LinkedIn scraping - 10,000 customers)
-  Capacity: $900/month (brand new AI coding tool)

He never attended a bootcamp. Never worked at FAANG. Never raised VC money.

Just pure copycat execution.

"You don't need to innovate," he told me. "Just see what's working and build your own version."

Here's the brutal truth they don't want you to know:

The most successful builders aren't inventors. They're professional thieves who steal proven ideas and execute them better.

Innovation is expensive. Imitation is profitable.

While everyone's chasing the next "revolutionary" breakthrough, Samuel builds boring tools that solve real problems people already pay for.

Speed beats originality. Execution beats innovation.

Stop trying to invent the wheel. Just build a better one.

Comment "COPY" if you want Samuel's exact validation framework
♻️ Repost if you think copying beats creating
👥 Follow me for more startup truths

P.S. This post was generated by Echo - the AI that turns youtube video into viral LinkedIn posts."""
]

# Combine all posts
all_posts = posts + batch2_posts

for post_text in all_posts:
    db_post = LinkedInPost(
        post_text=post_text.strip(),
        post_type="training_example"
    )
    db.add(db_post)

db.commit()
print(f'✅ Training complete! Added {len(all_posts)} posts')
print(f'Total posts in database: {db.query(LinkedInPost).count()}')
db.close()
