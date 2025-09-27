#Database definition using SQL Alchemy

from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Report(Base):
    __tablename__ = "reports"
    id: int = Column(Integer, primary_key=True)
    drug: str = Column(String, index=True)
    adverse_events: list[str] = Column(JSON)
    severity: str = Column(String, index=True)
    outcome: str = Column(String)
    outcome_translated = Column(String, default="unknown")
    raw_report: str = Column(String)
    doctor = Column(String,  index=True)



