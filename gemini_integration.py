from google import genai
import os
from dotenv import load_dotenv

# Load env
load_dotenv()

# Create client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def confirm_crash(accel_value, gyro_value):
    prompt = f"""
    Accelerometer: {accel_value}
    Gyroscope: {gyro_value}
    Is this a crash? Reply only YES or NO.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text.strip()


print(confirm_crash(25, 12))