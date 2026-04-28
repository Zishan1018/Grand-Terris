import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://grand-terris-default-rtdb.asia-southeast1.firebasedatabase.app'
})

def send_crash_alert(accel_value, gyro_value, lat, lon):
    ref = db.reference('crashes')
    ref.push({
        'accelerometer': accel_value,
        'gyroscope': gyro_value,
        'latitude': lat,
        'longitude': lon,
        'status': 'CRASH DETECTED',
        'timestamp': {'.sv': 'timestamp'}
    })

    print("🚨 Crash alert sent to Firebase!")

    return lat, lon

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://grand-terris-default-rtdb.asia-southeast1.firebasedatabase.app'
    })