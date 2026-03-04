from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def llm_check(message):

    prompt = f"""
You are a fact-checking assistant.

Analyze the following claim and determine if it is likely fake news.

Claim: {message}

Respond in this format:

Verdict: Fake / Possibly True / Unverified
Reason: short explanation
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=120,
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:
        print("LLM error:", e)
        return "AI analysis unavailable right now."