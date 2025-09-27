# Mini Regulatory Report Assistant - Frontend

This is the **frontend application** for the Mini Regulatory Report Assistant. It is built with **Next.js (React)** and communicates with the backend API to process, display, and translate medical reports.

## Table of Contents
1. [Features](#features)
2. [Folder Structure](#folder-structure)
3. [Installation](#installation)
4. [Running the App](#running-the-app)
5. [Using the Application](#using-the-application)
6. [Screenshots](#screenshots)
7. [Dependencies](#dependencies)
8. [Notes](#notes)

---

## Features
- Input form for medical reports, doctor name, and language selection.
- Processes reports using the backend API.
- Displays structured report data in **cards** and **tables**.
- Shows **report history** with past submissions.
- Charts showing **severity distribution** of processed reports.
- Optional translation of outcomes (French / Swahili).

---

## Folder Structure
```
/frontend
│
├─ /components
│   ├─ Form.tsx          # Input form for submitting reports
│   ├─ Table.tsx         # Table component for displaying report history
│   ├─ Card.tsx          # Card component to display individual processed report
│   ├─ severityChart.tsx # Chart component for severity distribution
│
├─ /contents
│   └─ siteContent.ts    # Form fields and table column definitions
│
├─ /lib
│   └─ report_api.ts     # API functions to communicate with backend
│
├─ /app
│   └─ index.tsx         # Main page containing form, history, and charts
│
├─ /styles
│   ├─ components.scss   # Stylesheet for the components 
│   └─ homePage.scss     # styleshet for the homepage
│
├─ package.json
└─ tsconfig.json
```

---

## Installation

Make sure you have **Node.js** installed.  

1. Navigate to the frontend folder:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
# or
yarn install
```

---

## Running the App

Start the development server:

```bash
npm run dev
# or
yarn dev
```

Open your browser at [http://localhost:3000](http://localhost:3000).

> Make sure your backend server is running at `http://localhost:8000`.

---

## Using the Application

1. Enter or paste a **medical report**.
2. Optionally provide the **doctor name**.
3. Select the **language** for translation (`en`, `fr`, or `sw`).
4. Click **Process Report**.
5. View processed results in **cards**.
6. Scroll down to see **report history** in a table.
7. Severity distribution is shown in a **bar chart**.

---

## Screenshots

(./screenshots/1.png)

(./screenshots/2.png)

(./screenshots/3.png)

(./screenshots/4.png)

---

## Dependencies
- React 18 / Next.js 15
- TypeScript
- Recharts (for charts)
- SCSS
- Axios / Fetch API (for backend communication)

---

## Notes
- The frontend communicates with the backend via JSON API. Make sure the backend is accessible.