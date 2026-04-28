import streamlit as st
import random
import time
import math

# ==============================
# 🚗 Crash Detection Logic
# ==============================
ACCEL_THRESHOLD = 20
GYRO_THRESHOLD = 10

def is_crash(accel, gyro):
    return accel > ACCEL_THRESHOLD and gyro > GYRO_THRESHOLD


# ==============================
# 📍 Mock GPS
# ==============================
def get_location():
    # Simulated Hyderabad location
    return 17.3850, 78.4867


# ==============================
# 🏥 Mock Hospitals
# ==============================
HOSPITALS = [
    {"name": "Apollo Hospital", "lat": 17.3850, "lon": 78.4867},
    {"name": "Yashoda Hospital", "lat": 17.4435, "lon": 78.3772},
    {"name": "Care Hospital", "lat": 17.4010, "lon": 78.4770},
    {"name": "KIMS Hospital", "lat": 17.4350, "lon": 78.4480},
]

def calculate_distance(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def find_nearest_hospital(lat, lon):
    nearest = None
    min_dist = float('inf')

    for h in HOSPITALS:
        dist = calculate_distance(lat, lon, h["lat"], h["lon"])
        if dist < min_dist:
            min_dist = dist
            nearest = h

    return nearest


# ==============================
# 📩 Fake SMS (for demo)
# ==============================
def send_sms_alert(message):
    print("\n📩 SMS SENT:")
    print(message)


# ==============================
# 🎨 UI Styling
# ==============================
st.set_page_config(page_title="Crash Detection", page_icon="🚗")

st.markdown("""
<style>
.big-title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: #ff4b4b;
}
.card {
    background-color: #1e1e1e;
    padding: 20px;
    border-radius: 15px;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🚗 Crash Detection System</p>', unsafe_allow_html=True)
st.write("Real-time accident detection & emergency response system")

# Sidebar
st.sidebar.title("⚙️ Settings")
runs = st.sidebar.slider("Simulation Runs", 1, 20, 10)

start = st.button("▶️ Start Simulation")

# ==============================
# 🚀 MAIN LOOP
# ==============================
if start:
    for _ in range(runs):

        accel = random.randint(0, 30)
        gyro = random.randint(0, 20)

        st.markdown(f"""
        <div class="card">
        📊 <b>Accel:</b> {accel} <br>
        🌀 <b>Gyro:</b> {gyro}
        </div>
        """, unsafe_allow_html=True)

        if is_crash(accel, gyro):

            st.markdown("""
            <div class="card" style="background-color:#ff4b4b; color:white;">
            ⚠️ CRASH DETECTED!
            </div>
            """, unsafe_allow_html=True)

            # Countdown
            st.write("⏳ Checking user...")
            for i in range(5, 0, -1):
                st.write(i)
                time.sleep(1)

            st.warning("🚨 Sending alert...")

            # GPS
            lat, lon = get_location()

            # Hospital
            hospital = find_nearest_hospital(lat, lon)

            crash_map = f"https://www.google.com/maps?q={lat},{lon}"
            hospital_map = f"https://www.google.com/maps?q={hospital['lat']},{hospital['lon']}"

            # Display
            st.success("📍 Location detected")
            st.markdown(f"[Open Crash Location]({crash_map})")

            st.success(f"🏥 Nearest Hospital: {hospital['name']}")
            st.markdown(f"[Navigate to Hospital]({hospital_map})")

            # Message
            message = f"""
🚨 CRASH ALERT!

Location: {crash_map}
Hospital: {hospital['name']} - {hospital_map}

Please check immediately!
"""

            send_sms_alert(message)

            st.success("📩 Alert Sent!")

            break

        else:
            st.info("✅ Normal movement")

        time.sleep(1)