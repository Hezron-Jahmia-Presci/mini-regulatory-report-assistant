export type ReportForm = {
  report: string;
  doctor?: string;
  language?: 'en' | 'fr' | 'sw'; 
};



export async function processReport(data: ReportForm, targetLanguage: 'en' | 'fr' | 'sw' = 'en') {
  const response = await fetch(`http://localhost:8000/reports/process?target_language=${targetLanguage}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),  
  });

  if (!response.ok) {
    throw new Error(`Error: ${response.statusText}`);
  }

  return response.json();
}

export async function getReportHistory(skip = 0, limit = 50) {
  const res = await fetch(`http://localhost:8000/reports/?skip=${skip}&limit=${limit}`);
  if (!res.ok) throw new Error(res.statusText);
  return res.json();
}


