import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

client = Client(
    os.getenv("TWILIO_SID"),
    os.getenv("TWILIO_AUTH")
)

def send_sms_alert(message):
    try:
        msg = client.messages.create(
            body=message,
            from_=os.getenv("TWILIO_PHONE"),
            to=os.getenv("EMERGENCY_PHONE")
        )
        print("✅ SMS sent:", msg.sid)
    except Exception as e:
        print("❌ SMS failed:", e)