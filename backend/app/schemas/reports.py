# request and response structure for the API

from pydantic import BaseModel
from typing import List, Optional

# request schema

class ReportRequest(BaseModel):
    report: str
    doctor: Optional[str] = None
    language: Optional[str] = "en"



# response schema
class ReportResponse(BaseModel):
    drug: str
    adverse_events: List[str]
    severity: str
    outcome: str
    outcome_translated: Optional[str] = None
    doctor: Optional[str] = None
    report: Optional[str] = None
