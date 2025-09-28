from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import reports
from app.models.reports import Base
from app.databases.db import engine
import os
from dotenv import load_dotenv

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mini Regulatory Report Assistant",
    description="Backend API for processing adverse event reports",
    version="1.0.0"
)

origins = os.getenv("CORS_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins if origins[0] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(reports.router)

@app.get("/")
def read_root():
    return {"message": "Backend is running 🚀"}
