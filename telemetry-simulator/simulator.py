import random
import time
import requests
import os

API = os.environ.get("API_URL", "http://api:5000/telemetry")
INTERVAL = float(os.environ.get("INTERVAL", "2"))
VEHICLE_ID = os.environ.get("VEHICLE_ID", "VEHICLE-001")

def generate_payload():
    return {
        "vehicle_id": VEHICLE_ID,
        "speed": random.randint(0, 160),
        "engine_temp": random.randint(60, 120),
        "battery_voltage": round(random.uniform(11.5, 14.8), 2),
        "fuel_level": random.randint(0, 100),
        "lat": round(18.5204 + random.uniform(-0.01, 0.01), 6),
        "lon": round(73.8567 + random.uniform(-0.01, 0.01), 6),
        "timestamp": int(time.time())
    }

if __name__ == "__main__":
    while True:
        data = generate_payload()
        try:
            r = requests.post(API, json=data)
            print("Sent:", data, "Status:", r.status_code)
        except Exception as e:
            print("Error:", e)
        time.sleep(INTERVAL)
