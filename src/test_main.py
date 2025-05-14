from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)


def test_get_mods():        
    with TestClient(app) as client:
        response = client.get("/mods")
        assert response.status_code == 200
        data = response.json()
        assert {"items", "mods"} & data.keys() != set()


def test_download():        
    # with TestClient(app) as client:
    for code in ["vFh38DUJqzzxhuz", "42Jo4ewFnASaG66", "Iql4uSFYThcN3vF"]:
        response = client.get("/download/" + code)
        assert response.status_code == 200
        print(response.headers.get("Content-Disposition"))
        assert response.headers.get("Content-Type") == "application/octet-stream"