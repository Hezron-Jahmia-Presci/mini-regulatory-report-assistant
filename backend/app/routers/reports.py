# control layer where FastAPI exposes endpoints and connects schenmas, services and CRUD together

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi import Query

from app.services.reports import process_and_translate, translate_text
from app.schemas.reports import ReportRequest, ReportResponse
from app.services.reports import process_report
from app.handlers.reports import (
    create_report,
    get_reports,
    get_report_by_id,
    update_report,
    delete_report,
    search_reports,
    filter_reports
)
from app.databases.db import get_db

router = APIRouter(
    prefix="/reports",
    tags=["reports"]
)

#PST/reports/process

@router.post("/process", response_model=ReportResponse)
def process_report_endpoint(
    request: ReportRequest,
    target_language: str = Query("en", pattern="^(en|fr|sw)$"),
    db: Session = Depends(get_db)
):
    try:
        processed_data = process_and_translate(
            report=request.report,
            target_language=target_language,
            doctor=request.doctor
        )

        create_report(db, processed_data, request.report)
        
        return processed_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))






# GET /reports/

@router.get("/", response_model=List[ReportResponse])
def get_reports_endpoint(
        skip: int = 0, 
        limit: int = 10, 
        db: Session = Depends(get_db)
    ):
        reports_list = get_reports(db, skip=skip, limit=limit)

        return [
            ReportResponse(
                drug=r.drug,
                adverse_events=r.adverse_events,
                severity=r.severity,
                outcome=r.outcome,
                outcome_translated=r.outcome_translated if hasattr(r, 'outcome_translated') else r.outcome
            )
            for r in reports_list
        ]


# GET /reports/{id}

@router.get("/{report_id}", response_model=ReportResponse)
def get_report_by_id_endpoint(
        report_id: int, 
        db: Session = Depends(get_db)
    ):
        report = get_report_by_id(db, report_id)
        if not report:
            raise HTTPException(status_code=404, detail="Report not found")
        
        return ReportResponse(
            drug=report.drug,
            adverse_events=report.adverse_events,
            severity=report.severity,
            outcome=report.outcome
        )


# PUT /reports/{id}

@router.put("/{report_id}", response_model=ReportResponse)
def update_report_endpoint(
        report_id: int, 
        update_data: ReportRequest, 
        db: Session = Depends(get_db)
    ):
        processed = process_report(update_data.report)
        updated_report = update_report(
              db, report_id, 
              processed
            )
        
        if not updated_report:
            raise HTTPException(status_code=404, detail="Report not found")
        
        return ReportResponse(
            drug=updated_report.drug,
            adverse_events=updated_report.adverse_events,
            severity=updated_report.severity,
            outcome=updated_report.outcome
        )


# DELETE /reports/{id}

@router.delete("/{report_id}", response_model=dict)
def delete_report_endpoint(
        report_id: int, 
        db: Session = Depends(get_db)
    ):
        success = delete_report(db, report_id)
        if not success:
            raise HTTPException(status_code=404, detail="Report not found")
        return {"detail": "Report deleted successfully"}


# GET /reports/search/

@router.get("/search/", response_model=List[ReportResponse])
def search_reports_endpoint(
    keyword: str = Query(..., min_length=1),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    results = search_reports(
        db, 
        keyword, 
        skip=skip, 
        limit=limit
    )

    return [
        ReportResponse(
            drug=r.drug,
            adverse_events=r.adverse_events,
            severity=r.severity,
            outcome=r.outcome
        )
        for r in results
    ]


# GET /reports/filter/

@router.get("/filter/", response_model=List[ReportResponse])
def filter_reports_endpoint(
    severity: Optional[str] = None,
    outcome: Optional[str] = None,
    drug: Optional[str] = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    results = filter_reports(
          db, 
          severity=severity, 
          outcome=outcome, 
          drug=drug, 
          skip=skip, 
          limit=limit
        )
    
    return [
        ReportResponse(
            drug=r.drug,
            adverse_events=r.adverse_events,
            severity=r.severity,
            outcome=r.outcome
        )
        for r in results
    ]


# GET /reports/translate/

@router.get("/translate/", response_model=dict)
def translate_report_endpoint(
    report_id: int = Query(..., description="ID of the report to translate"),
    target_language: str = Query(..., pattern="^(fr|sw)$"),
    db: Session = Depends(get_db)
):
    report = get_report_by_id(db, report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    try:
        translated = translate_text(report.outcome, target_language)
        report.outcome_translated = translated
        update_report(db, report_id, {"outcome_translated": translated})

        return {
            "original": report.outcome,
            "translated": translated,
            "language": target_language
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
