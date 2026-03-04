from fastapi import FastAPI,Request,Response
from app.database import messages_collection
from twilio.twiml.messaging_response import MessagingResponse

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
@app.post("/webhook/whatsapp")
async def whatsapp_webhook(request: Request):

    form_data = await request.form()
    incoming_msg = form_data.get("Body")

    resp = MessagingResponse()
    msg = resp.message()
    msg.body(f"You said: {incoming_msg}")

    return Response(content=str(resp), media_type="application/xml")