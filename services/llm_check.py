import openai
from app.config import settings

openai.api_key = settings.OPENAI_API_KEY

def llm_check(message):

    prompt = f"""
Determine if the following claim is likely fake news.

Claim: {message}

Respond with:
Fake / Possibly True / Unverified
and give a short explanation.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content