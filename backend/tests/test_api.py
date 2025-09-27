import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_process_report_endpoint():
    payload = {"report": "Patient experienced severe headache after taking Drug X. Patient recovered."}
    response = client.post("/reports/process?lang=fr", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["drug"] == "Drug X"
    assert "headache" in data["adverse_events"]
    assert data["severity"] == "severe"
    assert data["outcome"] == "recovered"
    assert data["outcome_translated"]  # should exist

def test_get_reports_endpoint():
    response = client.get("/reports/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
