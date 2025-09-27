import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.reports import Base, Report
from app.schemas.reports import ReportRequest, ReportResponse
from app.handlers.reports import create_report, get_reports, update_report, delete_report

# Setup in-memory SQLite for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_create_and_get_report(db):
    data = {
        "drug": "Drug X",
        "adverse_events": ["nausea"],
        "severity": "severe",
        "outcome": "recovered"
    }
    create_report(db, data, "raw text")
    results = get_reports(db)
    assert len(results) == 1
    assert results[0].drug == "Drug X"

def test_update_report(db):
    data = {"drug": "Drug Y", "adverse_events": [], "severity": "mild", "outcome": "ongoing"}
    report = create_report(db, data, "raw text")
    updated = update_report(db, report.id, {"severity": "severe"})
    assert updated.severity == "severe"

def test_delete_report(db):
    data = {"drug": "Drug Z", "adverse_events": [], "severity": "mild", "outcome": "ongoing"}
    report = create_report(db, data, "raw text")
    success = delete_report(db, report.id)
    assert success is True
    results = get_reports(db)
    assert results == []
