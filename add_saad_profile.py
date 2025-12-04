from database import SessionLocal, LinkedInPost, ProfileData

db = SessionLocal()

# Add profile information
profile = ProfileData(
    name="Muhammad Saad Zaheer",
    headline="Founder | AI Strategy | Digital Transformation | Enterprise AI Solutions | Secure & Safe AI Solutions | B2G & B2B | Working on Vision 2030",
    about="""Co-Founder at Remote Stack AI | Your AI Transformation Partner
Empowering businesses with cutting-edge AI solutions that drive innovation and growth.

Services: AI Product Development, AI Consulting, Custom AI Solutions, Transformational Results

Industry Expertise: Healthcare, Finance & Banking, Retail & E-commerce, Manufacturing & Supply Chain, Construction, Energy & Utilities, Telecommunications, Automotive & Transportation, Education & EdTech, Consumer & Sports

Technology Stack: Computer Vision (OpenCV, TensorFlow, PyTorch), NLP (SpaCy, NLTK, Hugging Face), Generative AI (GPT models), Machine Learning, Deep Learning, LLMs (GPT-4, BERT, OpenAI APIs), RAG, LangChain, LLaMA""",
    current_position="CEO & Co-Founder at Remote Stack AI | Co-Founder & Director of Defense Intelligence at Falcon Sight | CEO & Founder at Nevox AI",
    location="Riyadh, Saudi Arabia"
)
db.add(profile)

# Add user's LinkedIn posts
user_posts = [
    """Strategic Defense Partnership between Saudi Arabia and Pakistan

🔸 The "Joint Strategic Defense Agreement" represents a significant step in strengthening defense cooperation between the Kingdom of Saudi Arabia and the Islamic Republic of Pakistan.

▪️ It establishes a framework for joint military collaboration, enhancing readiness and interoperability.
▪️ It reinforces the principle of collective deterrence, declaring that an attack on either nation will be regarded as an attack on both.
▪️ It reflects a shared commitment to regional stability and mutual security in an increasingly complex geopolitical environment.

🔸 Beyond defense, this agreement symbolizes a deeper strategic alignment — ensuring both nations stand united against external threats while advancing long-term regional balance.

#SaudiArabia #Pakistan #DefenseStrategy #JointSecurity #Geopolitics #StrategicPartnership #RegionalStability""",

    """🚀 𝐏𝐚𝐤𝐢𝐬𝐭𝐚𝐧𝐢 𝐒𝐭𝐚𝐫𝐭𝐮𝐩𝐬: 𝐓𝐢𝐦𝐞 𝐭𝐨 𝐌𝐨𝐯𝐞 𝐅𝐚𝐬𝐭! 🌟

The Saudi market is growing at lightning speed—new opportunities are emerging every day, and international startups are in high demand! 🇸🇦

I'm part of a 𝐑𝐢𝐲𝐚𝐝𝐡-𝐛𝐚𝐬𝐞𝐝 𝐬𝐭𝐚𝐫𝐭𝐮𝐩 𝐢𝐧𝐜𝐮𝐛𝐚𝐭𝐨𝐫, and we're looking for innovative Pakistani AI startups ready to launch and scale in Saudi Arabia.

We'll support you with:
✅ Market entry strategy
✅ Mentorship & business guidance
✅ Tech, legal, and operational support
✅ Connections with investors & key partners

⏳ The time to act is now! Don't let this fast-moving market pass you by.

🎯 Apply here: https://lnkd.in/dvpRQ7Vj

#PakistaniStartups #SaudiArabia #StartupExpansion #Incubator #Innovation #Entrepreneurship""",

    """𝐖𝐡𝐞𝐧 𝐭𝐡𝐞 𝐟𝐨𝐫𝐦𝐞𝐫 𝐂𝐓𝐎 𝐨𝐟 𝐑𝐢𝐲𝐚𝐝𝐡 𝐁𝐚𝐧𝐤 𝐬𝐚𝐲𝐬,
"𝑰𝒏 𝒃𝒂𝒏𝒌𝒊𝒏𝒈, 𝒕𝒉𝒆 𝒓𝒆𝒂𝒍 𝒊𝒏𝒏𝒐𝒗𝒂𝒕𝒊𝒐𝒏 𝒊𝒔𝒏'𝒕 𝒇𝒍𝒂𝒔𝒉𝒚 — 𝒊𝒕'𝒔 𝒆𝒇𝒇𝒊𝒄𝒊𝒆𝒏𝒕,"

You pause and listen.

I had the privilege of meeting Rashed AlOthman, a seasoned tech leader who helped build one of the most sophisticated banking infrastructures in the region.

We didn't talk buzzwords.
We talked systems that save minutes, because minutes saved at scale = millions in value.

We talked lean architectures, automation, and AI that doesn't just look good in a demo — it works under pressure.

His mantra:
"𝑬𝒇𝒇𝒊𝒄𝒊𝒆𝒏𝒄𝒚 𝒊𝒔 𝒕𝒉𝒆 𝒄𝒐𝒎𝒑𝒆𝒕𝒊𝒕𝒊𝒗𝒆 𝒆𝒅𝒈𝒆 𝒏𝒐 𝒐𝒏𝒆 𝒕𝒂𝒍𝒌𝒔 𝒂𝒃𝒐𝒖𝒕 𝒆𝒏𝒐𝒖𝒈𝒉."

In a market like Saudi Arabia — where fintech is exploding — his insights felt like a blueprint for sustainable innovation.

Grateful for the time and wisdom, Rashed.

The more I meet leaders like you, the clearer it becomes:
"𝑻𝒉𝒆 𝒇𝒖𝒕𝒖𝒓𝒆 𝒃𝒆𝒍𝒐𝒏𝒈𝒔 𝒕𝒐 𝒕𝒉𝒆 𝒇𝒂𝒔𝒕, 𝒏𝒐𝒕 𝒋𝒖𝒔𝒕 𝒕𝒉𝒆 𝒃𝒊𝒈."

#Efficiency #BankingInnovation #FintechSaudi #AI #DigitalTransformation #RemoteStackAI #Leadership #RiyadhBank #TimeIsMoney #SaudiVision2030 #TechLeadership""",

    """Today's sell-off is not based on models but on moats.

DeepSeek demonstrates that competitive models 1) do not need as much hardware to train or infer, 2) can be open-sourced, and 3) can utilize hardware other than NVIDIA (in this case, AMD).

The market forecast was that NVIDIA and third parties supporting NVIDIA data centers would be the dominant players for at least 18-24 months. DeepSeek's arrival made already tense investors rethink their assumptions on market competitiveness timelines.

Today's "DeepSeek selloff" in the stock market -- attributed to DeepSeek V3/R1 disrupting the tech ecosystem -- is another sign that the application layer is a great place to be. The foundation model layer being hyper-competitive is great for people building applications.""",

    """The drama at OpenAI continues! 🍿

Reports suggest OpenAI is considering triggering their "AGI achieved" clause to break free from their contract with Microsoft and gain leverage to renegotiate compute pricing. 😳

This might explain the recent wave of leadership departures at OpenAI. Just recently, CTO Mira Murati, Chief Research Officer Bob McGrew, and VP of Research Barret Zoph all exited the world's most valuable AI startup.

It seems they've already cashed in and aren't sticking around for what could turn into a massive legal battle.

Unfolding chaos! 🍿""",

    """Sam Altman was the President of YC.

Startup advice given at YC:
- Launch right away
- Launch 1st version you're embarrassed about
- Raise very little capital up front
- Don't take big R&D risk
- Find PMF quickly, with 'something'

Versus how he launched OpenAI:
- Raised 1B dollars of capital before any PMF
- Took 4 to 5 years after launch to release
- Didn't talk to users upon release

Moral of the story? Be careful of textbook advice, no matter who it came from.

Prioritise finding smart people with solid analytical skills, instead.

Then, make educated bets together.""",

    """OpenAI's monthly revenue surged to $300M in August, marking a 1700% increase since early 2023, with projections of $3.7B in annual sales this year. The company anticipates revenue skyrocketing to $11.6B next year, despite forecasting a $5B loss this year.

With revenues growing at such a rapid pace, OpenAI is positioned to attract investors to cover its losses. It's not every day you encounter a company with legitimate potential for a $1 trillion+ valuation, and OpenAI is certainly one of those rare opportunities.

Thrive, as the lead investor, has a unique advantage: the option to invest an additional $1 billion at the current $150 billion valuation until 2025. Considering OpenAI's explosive growth, this could be a highly lucrative opportunity for Thrive. Regardless of the naysayers, OpenAI's valuation is poised to rise significantly—and fast.

Additionally, OpenAI has two years to convert to a for-profit model, or its funding will turn into debt, per deal terms. Shifting to a for-profit structure is a wise decision, as for-profit organizations tend to be more sustainable and effective in the long run.

#OpenAI #ArtificialIntelligence #AI #TechGrowth #RevenueGrowth #InvestmentOpportunity #ForProfit #BusinessStrategy #StartupValuation #TechInnovation #VentureCapital #FutureOfAI #TechInvestments #DisruptiveTechnology #AIRevolution""",

    """Big News in the AI World! 🚨

Apple has taken a monumental step by fully embracing open-source with their latest release: DCLM 7B. This 7-billion-parameter LLM is not only open-source but includes everything—model weights, training code, and dataset.

Here's why this matters:

🔹 Performance: DCLM 7B outperforms several benchmarks, including Mistral, Qwen2, and Gemma.
🔹 Training Data: Trained on 2.5 trillion tokens with a 2048 context window, using data from Common Crawl.
🔹 Data Curation: The release features an in-depth explanation of the data curation process, providing valuable insights into LLM training.
🔹 Framework: Introduces the DataComp-LM framework, which will aid future experiments with data curation strategies.

This move signifies a major shift in Apple's AI strategy towards open-source and highlights the growing trend of smaller models. It also hints at exciting developments in on-device AI.

The future of AI is indeed looking more open and collaborative!

#AppleOpenSource #DCLM7B #AIRevolution #OpenSourceAI #TechBreakthrough #AIInnovation #DataComp #MachineLearning #AIModels #TechTrends #AppleTech #LanguageModels #AIResearch #FutureOfAI #OnDeviceAI""",

    """Artificial Intelligence identifies breast cancer 5 years before onset.

MIT researchers have created a system named Mirai that forecasts the likelihood of developing breast cancer.

How it Works:
* A mammogram image is processed through an image encoder.
* Established risk factors are assessed using existing models.
* The data is then utilized to estimate the patient's risk of developing cancer over the next 5 years.

Source: Science.org

_________________________________________

We at Remote Stack AI have developed a system that can detect lung cancer. DM us for more information.""",

    """The AI landscape is rapidly evolving, with fierce competition driving down costs.

Meta recently unveiled their Llama 3.1 model, which delivers GPT-4-level performance at an exceptionally low cost and offers the capability to train smaller, specialized models. Shortly after, OpenAI announced that GPT-4o mini fine-tuning is now available for free for the next two months.

For businesses leveraging AI, this development has two key implications:

Decreasing Token Costs: Expect further reductions in token costs for large language models (LLMs). The competitive landscape has diminished the pricing power of any single vendor, so adjust your AI business cases accordingly.

Rethink Proprietary LLMs: Consider moving away from proprietary LLMs offered by smaller vendors. Companies such as Cohere and AlephAlpha, and similar startups, may struggle to survive in the long term or may operate in a niche, higher-cost market. It is akin to favoring Solaris when Windows, Mac, and Linux have become dominant.

The model of building and selling LLMs is no longer sustainable.
(If it ever was.)

However, for businesses integrating LLMs into their operations, the current environment presents an unparalleled opportunity. This is the moment to gain a significant competitive advantage over the next five years.

#AI #ArtificialIntelligence #LLM #MachineLearning #MetaAI #OpenAI #GPT4 #BusinessStrategy #AITrends #TechInnovation #DigitalTransformation #CompetitiveAdvantage #AIAdoption #TechTrends #FutureOfAI #DataScience #AIImpact #BusinessGrowth #AIInsights""",

    """With a $1.5 trillion pipeline of projects, Saudi Arabia's construction sector continues to be the largest across the GCC region.

As we settle into 2024, the construction space appears to be going from strength to strength, pulling in a stronger influx of businesses and public investments.

Find out the most exciting opportunities for international companies in this sector: https://lnkd.in/dCHq4AFJ

#AstroLabs #Construction #SaudiArabia #GigaProjects #SaudiConstruction""",

    """Transform Your Business with AI-Powered Chatbots! 🤖

In today's digital age, staying ahead means embracing innovation. At RemoteStack, we believe that AI-powered chatbots are game-changers for businesses aiming to enhance customer experience and operational efficiency.

🔹 24/7 Customer Support: Our chatbots ensure your customers receive instant, round-the-clock assistance, boosting satisfaction and loyalty.
🔹 Cost Efficiency: Automate routine tasks and reduce operational costs, freeing up resources for strategic initiatives.
🔹 Scalability: Handle thousands of interactions simultaneously, effortlessly scaling with your business growth.
🔹 Data-Driven Insights: Gain valuable insights into customer behavior and preferences, driving more personalized and effective engagement.
🔹 Boost Sales: Engage customers proactively, recommend products, and guide them through the purchasing journey, increasing conversion rates.
🔹 Operational Efficiency: Streamline internal processes, allowing your team to focus on what truly matters.

Join us in leveraging advanced AI technologies to transform your business. Let's create exceptional customer experiences and drive growth together

If you want to build something with Chatbots or want to use AI in your business CONTACT US at saad@remotestack.org"""
]

# Add all user posts with user_profile tag
for post_text in user_posts:
    db_post = LinkedInPost(
        post_text=post_text.strip(),
        post_type="user_profile"
    )
    db.add(db_post)

db.commit()

# Get stats
training_count = db.query(LinkedInPost).filter(
    LinkedInPost.post_type == "training_example"
).count()

user_count = db.query(LinkedInPost).filter(
    LinkedInPost.post_type == "user_profile"
).count()

print("=" * 60)
print("✅ PROFILE DATA ADDED SUCCESSFULLY!")
print("=" * 60)
print(f"\n📊 Training Statistics:")
print(f"   • Viral training examples: {training_count} posts")
print(f"   • Your profile posts: {user_count} posts")
print(f"   • Total learning data: {training_count + user_count} posts")
print("\n🎯 The AI Now Knows:")
print("   1. What makes posts go VIRAL (from training examples)")
print("   2. YOUR voice, tone, and style (from your posts)")
print("   3. Saudi Arabia market context")
print("   4. Vision 2030 alignment")
print("   5. Your expertise areas (AI, Defense, Fintech, etc.)")
print("\n🚀 Ready to Generate Viral Content!")
print("   Run: python simple_main.py")
print("   Open: http://localhost:8000")
print("\n💡 The AI will blend:")
print("   ✓ Viral hooks and engagement patterns")
print("   ✓ Your professional tone and expertise")
print("   ✓ Saudi market relevance")
print("   = Posts that sound like YOU but perform like VIRAL content")
print("=" * 60)

db.close()
