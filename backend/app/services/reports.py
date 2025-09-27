import re
from typing import List, Dict
import spacy
from translate import Translator

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Known lists
KNOWN_ADVERSE_EVENTS = ["nausea", "headache", "dizziness", "fatigue", "vomiting", "rash", "fever", "cough"]


KNOWN_OUTCOMES = {
    "recovered": ["recovered", "healed", "got better", "improved"],
    "hospitalized": ["hospitalized", "admitted", "in hospital"],
    "fatal": ["fatal", "died", "dead", "passed away", "deceased"],
    "ongoing": ["ongoing", "still sick", "not improved"],
    "unknown": []
}



# Extractors

def extract_drug(report: str) -> str:
    report = report.lower()
    patterns = [
        r"taking ([\w\s]+?)(?:,| and|\.|$)",
        r"took ([\w\s]+?)(?:,| and|\.|$)",
        r"swallowing ([\w\s]+?)(?:,| and|\.|$)",
        r"swallowed ([\w\s]+?)(?:,| and|\.|$)",
        r"overdosing on ([\w\s]+?)(?:,| and|\.|$)",
        r"overdose of ([\w\s]+?)(?:,| and|\.|$)",
        r"on ([\w\s]+?)(?:,| and|\.|$)"
    ]
    for pattern in patterns:
        match = re.search(pattern, report)
        if match:
            return match.group(1).strip()
    return "unknown"



def extract_adverse_events(report: str) -> List[str]:
    lowered = report.lower()
    return [event for event in KNOWN_ADVERSE_EVENTS if event in lowered]


def extract_severity(report: str) -> str:
    lowered = report.lower()
    if "severe" in lowered or "critical" in lowered:
        return "severe"
    elif "moderate" in lowered:
        return "moderate"
    elif "mild" in lowered or "light" in lowered:
        return "mild"
    return "moderate"


def extract_outcome(report: str) -> str:
    lowered = report.lower()
    for outcome, keywords in KNOWN_OUTCOMES.items():
        if any(word in lowered for word in keywords):
            return outcome
    return "unknown"


def extract_adverse_events_nlp(report: str) -> List[str]:
    doc = nlp(report.lower())
    found_events = set()

    for token in doc:
        if token.lemma_ in KNOWN_ADVERSE_EVENTS:
            found_events.add(token.lemma_)

    return list(found_events)


# Core processing

def process_report(report: str, doctor: str = None) -> dict:
    return {
        "drug": extract_drug(report),
        "adverse_events": extract_adverse_events_nlp(report),
        "severity": extract_severity(report),
        "outcome": extract_outcome(report),
        "outcome_translated": extract_outcome(report),
        "doctor": doctor
    }



# Translation

def translate_text(text: str, target_language: str) -> str:
    if target_language not in ['fr', 'sw']:
        raise ValueError("Unsupported target language. Use 'fr' or 'sw'.")
    
    translator = Translator(to_lang=target_language)
    translated = translator.translate(text)

    if not translated:
        return text
    return translated



def process_and_translate(report: str, target_language: str = "en", doctor: str = None) -> dict:
    processed = process_report(report)
    processed["doctor"] = doctor or "Unknown"
    try:
        if target_language == "en":
            processed["outcome_translated"] = processed["outcome"]
        elif target_language in ["fr", "sw"]:
            processed["outcome_translated"] = translate_text(processed["outcome"], target_language)
        else:
            raise ValueError("Unsupported target language. Use 'en', 'fr', or 'sw'.")
    except Exception as e:
        processed["outcome_translated"] = processed["outcome"]
        print("Translation failed:", e)

    if "adverse_events" not in processed or processed["adverse_events"] is None:
        processed["adverse_events"] = []

    if "severity" not in processed or processed["severity"] is None:
        processed["severity"] = "moderate"

    if "outcome" not in processed or not processed["outcome"]:
        processed["outcome"] = "unknown"

    return processed


