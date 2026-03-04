from fastapi import FastAPI,Request,Response
from app.database import messages_collection
from twilio.twiml.messaging_response import MessagingResponse
from services.fact_check import check_fact

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

    # 1️⃣ Get message from Twilio
    form_data = await request.form()
    incoming_msg = form_data.get("Body")

    # 2️⃣ Run fact check
    result = check_fact(incoming_msg)

    if result:
        reply = f"""
⚠ Fact Check Result

Rating: {result['result']}
Source: {result['source']}
"""
    else:
        reply = "⚠ No verified fact check found."

    # 3️⃣ Send response back to WhatsApp
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(reply)

    return Response(content=str(resp), media_type="application/xml")