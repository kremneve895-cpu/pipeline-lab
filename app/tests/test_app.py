from app import app

def test_index():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert r.get_json()["message"] == "pipeline-lab demo app"

def test_health():
    client = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"

def test_index_returns_json():
    client = app.test_client()
    r = client.get("/")
    assert r.is_json
