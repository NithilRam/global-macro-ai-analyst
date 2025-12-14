print("STARTING SCRIPT")

from openai import OpenAI

client = OpenAI()

# --- Prompt template (your framework) ---
prompt_template = """
You are a global macro-financial analyst supporting an investment and strategy team.

Your task is to analyze how the following major geopolitical event and/or risks can affect financial
markets in the United States and the Eurozone. The focus should be on how
geopolitical developments are manifested through economic conditions, policy
constraints, and risk perception to impact market outcomes.

GEOPOLITICAL EVENT / RISK:
{event}

Write your analysis for an internal investment or strategy committee.

Use the following framework:

1. GEOPOLITICAL SHOCK
   - Brief description of the geopolitical event or risk
   - Primary transmission channels (e.g., energy supply, trade, sanctions,
     political uncertainty, global risk sentiment)

2. MACRO & POLICY IMPLICATIONS
   - Impact on inflation and cost pressures
   - Implications for economic growth
   - Constraints or considerations for central bank policy
   - Differences in exposure between the United States and the Euro Area

3. MARKET TRANSMISSION
   - Equities: valuation multiples, earnings sensitivity, and risk sentiment
   - Fixed Income: yield levels, spreads, and duration considerations
   - Foreign Exchange: EUR/USD dynamics and cross-border capital flows

4. DECISION IMPLICATIONS
   - Relative risks and opportunities between the US and Europe
   - Key uncertainties and downside scenarios
   - High-level strategic considerations for investors and firms

Write in a concise, professional investment memo style.
Avoid political commentary, normative judgments, price forecasts, or specific
trade recommendations.
Focus on clear financial reasoning and structured analysis.
"""

# --- Choose an event (edit this anytime) ---
event = """
Yemeni instability and Houthi attacks on commercial shipping in the Red Sea and Bab el-Mandeb Strait
have increased shipping insurance costs, forced rerouting around the Cape of Good Hope, and raised
risks to global supply chains and energy flows into Europe.
""".strip()

prompt = prompt_template.format(event=event)

# --- Call the LLM ---
response = client.responses.create(
    model="gpt-4o-mini",
    input=prompt,
)

memo = response.output_text

# --- Output ---
print(memo)

with open("generated_memo.md", "w", encoding="utf-8") as f:
    f.write(memo)

print("\nSaved to generated_memo.md")
