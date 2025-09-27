# Mini Regulatory Report Assistant

A full-stack application simulating a regulatory report assistant for pharmacovigilance. Built with **FastAPI** for the backend and **Next.js (React)** for the frontend, this project extracts structured information from medical reports, supports translations, and displays processed data with charts and tables.

---

## Table of Contents

- [Features](#features)  
- [Backend](#backend)  
  - [Setup](#backend-setup)  
  - [API Endpoints](#api-endpoints)  
- [Frontend](#frontend)  
  - [Setup](#frontend-setup)  
  - [UI Features](#ui-features)  
- [Screenshots](#screenshots)  
- [Usage](#usage)  
- [License](#license)  

---

## Features

- Extracts structured fields from raw medical reports:
  - Drug name  
  - Adverse events  
  - Severity (mild, moderate, severe)  
  - Outcome (recovered, ongoing, fatal)  
- Stores processed reports in a **SQLite** database  
- Translation support for outcomes (English → French / Swahili)  
- Frontend displays:
  - Processed reports in cards  
  - Report history in a table  
  - Severity distribution chart  

---

## Backend

### Tech Stack

- Python 3.x  
- FastAPI  
- SQLAlchemy  
- SQLite  
- spaCy (for NLP)  
- translate (for multilingual support)  

### Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### API Endpoints

| Endpoint | Method | Description | Input | Output |
|----------|--------|-------------|-------|--------|
| `/reports/process` | POST | Process a medical report | JSON: `{ "report": "...", "doctor": "Dr. X", "language": "en" }` | JSON: `{ "drug": "...", "adverse_events": [...], "severity": "...", "outcome": "...", "outcome_translated": "..." }` |
| `/reports` | GET | Fetch processed report history | query params: `skip`, `limit` | JSON array of reports |
| `/reports/{id}` | GET | Fetch report by ID | - | JSON report |
| `/reports/{id}` | PUT | Update report | JSON update fields | Updated report |
| `/reports/{id}` | DELETE | Delete report | - | `true` / `false` |

---

## Frontend

### Tech Stack

- Next.js (React, TypeScript)  
- Recharts (charts)  
- Tailwind CSS (styling)  

### Setup

```bash
cd frontend
npm install
npm run dev
```

### UI Features

- **Form**: Input or paste medical reports, select language, add doctor name  
- **Cards**: Displays structured data from processed reports  
- **Table**: Shows report history with drug, adverse events, severity, outcome  
- **Chart**: Bar chart of severity distribution  

---

## Screenshots

![Screenshot 1](frontend/public/1.png)
 
![Screenshot 2](frontend/public/2.png)

![Screenshot 3](frontend/public/3.png) 

![Screenshot 4](frontend/public/4.png)

---

## Usage

1. Start backend:
   ```bash
   uvicorn main:app --reload
   ```
2. Start frontend:
   ```bash
   npm run dev
   ```
3. Open browser: [http://localhost:3000](http://localhost:3000)  
4. Enter/paste a medical report, select language, click **Process Report**  
5. View processed data, report history, and charts  

---

## License

MIT License © [Jahmia Hezron Presci]

