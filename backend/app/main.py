from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import reports
from app.models.reports import Base
from app.databases.db import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mini Regulatory Report Assistant",
    description="Backend API for processing adverse event reports",
    version="1.0.0"
)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] for all origins
    allow_credentials=True,
    allow_methods=["*"],    # allow GET, POST, PUT, etc.
    allow_headers=["*"],    # allow headers like Content-Type
)


app.include_router(reports.router)


@app.get("/")
def read_root():
    return {"message": "Backend is running 🚀"}
