from fastapi import FastAPI,Request,Response
from app.database import messages_collection
from twilio.twiml.messaging_response import MessagingResponse
from services.fact_check import check_fact
from services.llm_check import llm_check
from utils.claim_extractor import extract_claim

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Fake News Bot Running"}

@app.get("/test-db")
async def test_db():

    await messages_collection.insert_one({
        "message": "MongoDB async test",
        "result": "test",
        "confidence": 1.0
    })

    return {"status": "Async data inserted"}



@app.post("/webhook/whatsapp")
async def whatsapp_webhook(request: Request):

    form_data = await request.form()
    incoming_msg = form_data.get("Body")

    print("Incoming message:", incoming_msg)

    claim = extract_claim(incoming_msg)

    result = check_fact(claim)

    if result:
        reply = f"""
⚠ Fact Check Result

Rating: {result['result']}
Source: {result['source']}
"""
    else:
        ai_result = llm_check(claim)

        reply = f"""
🤖 AI Analysis

{ai_result}
"""

    await messages_collection.insert_one({
        "original_message": incoming_msg,
        "claim": claim,
        "result": reply
    })

    resp = MessagingResponse()
    msg = resp.message()
    msg.body(reply)

    return Response(content=str(resp), media_type="application/xml")