from fastapi import FastAPI, Request, Response
from twilio.twiml.messaging_response import MessagingResponse
from services.fact_check import check_fact
from services.llm_check import llm_check
from utils.claim_extractor import extract_claim

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Fake News Bot Running"}

@app.post("/webhook/whatsapp")
async def whatsapp_webhook(request: Request):

    form_data = await request.form()
    incoming_msg = form_data.get("Body")

    print("Incoming message:", incoming_msg)

    if not incoming_msg:
        incoming_msg = "No text message received"

    claim = extract_claim(incoming_msg)

    result = check_fact(claim)

    if result:
        reply = f"""
⚠ Fact Check Result

Rating: {result['result']}
Source: {result['source']}
"""
    else:
        try:
            ai_result = llm_check(claim)
        except Exception as e:
            print("LLM error:", e)
            ai_result = "AI analysis unavailable right now."

        reply = f"""
🤖 AI Analysis

{ai_result}
"""

    resp = MessagingResponse()
    msg = resp.message()
    msg.body(reply)

    return Response(content=str(resp), media_type="application/xml")