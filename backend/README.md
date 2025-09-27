# Mini Regulatory Report Assistant – Backend

This is the **backend service** for the Mini Regulatory Report Assistant, built with **FastAPI**. It processes medical reports, extracts structured information (drug, adverse events, severity, outcome), saves reports to a **SQLite database**, and supports **translation** of outcomes.

---

## Features

- **POST `/reports/process`** – Process a medical report and extract structured fields.  
- **GET `/reports`** – Retrieve history of processed reports.  
- **GET `/reports/translate`** – Translate an outcome into French or Swahili.  
- **SQLite database** – Stores processed reports for retrieval.  
- Uses **spaCy** for NLP extraction and **translate** library for translations.

---

## Tech Stack

- **Python 3.10+**  
- **FastAPI** for API endpoints  
- **SQLAlchemy** + **SQLite** for persistence  
- **spaCy** for NLP  
- **translate** library for multilingual support

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/mini-regulatory-report.git
cd mini-regulatory-report/backend
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Start the API

```bash
uvicorn app.main:app --reload
```

The backend will run at `http://127.0.0.1:8000`.

---

## API Endpoints

### **1. Process Report**

**POST** `/reports/process?target_language=<en|fr|sw>`

**Request Body**

```json
{
  "report": "Patient experienced severe nausea and headache after taking Drug X. Patient recovered.",
  "doctor": "Dr. Kim",
  "language": "en"
}
```

**Response Example**

```json
{
  "drug": "Drug X",
  "adverse_events": ["nausea", "headache"],
  "severity": "severe",
  "outcome": "recovered",
  "outcome_translated": "recovered",
  "doctor": "Dr. Kim",
  "report": "Patient experienced severe nausea and headache after taking Drug X. Patient recovered."
}
```

---

### **2. Get Reports History**

**GET** `/reports?skip=0&limit=10`

**Response Example**

```json
[
  {
    "drug": "Drug X",
    "adverse_events": ["nausea", "headache"],
    "severity": "severe",
    "outcome": "recovered",
    "outcome_translated": "recovered",
    "doctor": "Dr. Kim",
    "report": "Patient experienced severe nausea and headache after taking Drug X. Patient recovered."
  }
]
```

---

### **3. Translate Outcome**

**GET** `/reports/translate?report_id=1&target_language=fr`

**Response Example**

```json
{
  "original": "recovered",
  "translated": "rétabli",
  "language": "fr"
}
```

---

## Database

- **SQLite** used for persistence (`backend/db.sqlite`).  
- Model fields: `id`, `drug`, `adverse_events`, `severity`, `outcome`, `outcome_translated`, `doctor`, `raw_report`.

---

## Screenshots

> Replace these with actual screenshots from your API testing or Swagger docs.  

- API docs:  
![API Docs](./screenshots/api_docs.png)  

- Sample processed report:  
![Processed Report](./screenshots/processed_report.png)

---

## Notes

- Ensure the SQLite file has write permissions.  
- If translations fail, the original outcome is returned.  
- You can test endpoints via **Postman**, **curl**, or **FastAPI Swagger UI** at `http://127.0.0.1:8000/docs`.