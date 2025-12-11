import requests

BASE = "http://localhost:5000"

def test_health():
    r = requests.get(BASE + "/health")
    assert r.status_code == 200
