import pytest
from app.services.reports import process_report, process_and_translate

def test_process_report_basic():
    report = "Patient experienced severe nausea after taking Drug X. Patient recovered."
    result = process_report(report)

    assert result["drug"] == "Drug X"
    assert "nausea" in result["adverse_events"]
    assert result["severity"] == "severe"
    assert result["outcome"] == "recovered"

def test_translate_text_french():
    report = "Patient recovered."
    result = process_and_translate(report, "fr")  # returns dict
    translated = result["outcome_translated"]     # get the translated string
    
    assert isinstance(translated, str)
    assert translated != "recovered"  # ensure it was translated


def test_translate_invalid_language():
    with pytest.raises(ValueError):
        process_and_translate("recovered", "xx")
