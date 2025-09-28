export type ReportForm = {
  report: string;
  doctor?: string;
  language?: 'en' | 'fr' | 'sw';
};

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function processReport(
  data: ReportForm,
  targetLanguage: 'en' | 'fr' | 'sw' = 'en'
) {
  const response = await fetch(
    `${API_URL}/reports/process?target_language=${targetLanguage}`,
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    }
  );

  if (!response.ok) {
    throw new Error(`Error: ${response.statusText}`);
  }

  return response.json();
}

export async function getReportHistory(skip = 0, limit = 50) {
  const res = await fetch(`${API_URL}/reports/?skip=${skip}&limit=${limit}`);
  if (!res.ok) throw new Error(res.statusText);
  return res.json();
}
