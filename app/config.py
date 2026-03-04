from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    MONGO_URI = os.getenv("MONGO_URI")
    DB_NAME = os.getenv("DB_NAME")

    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

    FACT_CHECK_API_KEY = os.getenv("FACT_CHECK_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

settings = Settings()