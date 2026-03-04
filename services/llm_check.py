from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def llm_check(message):

    prompt = f"""
Determine if the following claim is fake news.

Claim: {message}

Respond with Fake / Possibly True / Unverified
and explain briefly.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content