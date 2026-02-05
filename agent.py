from openai import OpenAI
client = OpenAI()

def analyze_events(events):
    text = "\n".join(
        f"{e['start'].get('dateTime','all-day')} - {e['summary']}"
        for e in events
    )

    prompt = f"""
You are a personal productivity agent.
Analyze today's meetings and:
- Summarize
- Detect conflicts
- Suggest priorities

Calendar:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
