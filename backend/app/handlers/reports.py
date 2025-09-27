# responsible for database operations like creating, fetching 

from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.reports import Base, Report

def create_report(
        db: Session, 
        report_data: dict,
        raw_report: str
    ) -> Report:
    db_report = Report(
        drug=report_data["drug"],
        adverse_events=report_data["adverse_events"],
        severity=report_data["severity"],
        outcome=report_data["outcome"],
        outcome_translated=report_data["outcome_translated"],
        doctor=report_data["doctor"],
        raw_report=raw_report
    )
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report


def get_reports(
        db: Session, 
        skip: int = 0, 
        limit: int = 10
    ) -> List[Report]:
    return db.query(Report).offset(skip).limit(limit).all()


def get_report_by_id(
        db: Session, 
        report_id: int
    ) -> Optional[Report]:
    return db.query(Report).filter(Report.id == report_id).first()


def update_report(
    db: Session,
    report_id: int,
    update_data: dict
) -> Optional[Report]:
    report = get_report_by_id(db, report_id)
    if not report:
        return None
    for key, value in update_data.items():
        if hasattr(report, key):
            setattr(report, key, value)
    db.commit()
    db.refresh(report)
    return report


def delete_report(
        db: Session, 
        report_id: int
    ) -> bool:
    report = get_report_by_id(db, report_id)
    if not report:
        return False
    db.delete(report)
    db.commit()
    return True


def search_reports(
        db: Session, 
        keyword: str, 
        skip: int = 0, 
        limit: int = 10
    ) -> List[Report]:
    return db.query(Report)\
             .filter(Report.raw_report.ilike(f"%{keyword}%"))\
             .offset(skip)\
             .limit(limit)\
             .all()


def filter_reports(
    db: Session,
    severity: Optional[str] = None,
    outcome: Optional[str] = None,
    drug: Optional[str] = None,
    skip: int = 0,
    limit: int = 10
) -> List[Report]:
    query = db.query(Report)
    if severity:
        query = query.filter(Report.severity == severity)
    if outcome:
        query = query.filter(Report.outcome == outcome)
    if drug:
        query = query.filter(Report.drug == drug)
    return query.offset(skip).limit(limit).all()
