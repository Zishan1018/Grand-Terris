from Crash_detection import is_crash
from firebase_setup import send_crash_alert
from location import get_location
from hospitals import find_nearest_hospital
from location import get_location
from sms_alert import send_sms_alert

import random
import time


def countdown():
    print("⏳ Are you okay?")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    return False  # simulate no response


# ✅ DEMO LOOP
for _ in range(10):

    accel = random.randint(0, 30)
    gyro = random.randint(0, 20)

    print(f"\n📊 Accel: {accel}, Gyro: {gyro}")




if is_crash(accel, gyro):
    print("⚠️ Crash detected!")

    if not countdown():
        print("🚨 Sending alert...")

        # 📍 Get GPS
        lat, lon = get_location()

        # 🏥 Find nearest hospital
        hospital = find_nearest_hospital(lat, lon)

        # 🗺️ Maps links
        crash_map = f"https://www.google.com/maps?q={lat},{lon}"
        hospital_map = f"https://www.google.com/maps?q={hospital['lat']},{hospital['lon']}"

        # 📩 Message
        message = f"""
🚨 CRASH ALERT!

📍 Your Location:
{crash_map}

🏥 Nearest Hospital:
{hospital['name']}
{hospital_map}

Please check immediately!
"""

        print(message)

        # 🔥 SMS
        from sms_alert import send_sms_alert
        send_sms_alert(message)

    else:
        print("User cancelled")

else:
    print("Normal movement")