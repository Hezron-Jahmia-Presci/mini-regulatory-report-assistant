"use client";

import { useEffect, useState } from "react";
import { getReportHistory, processReport, ReportForm } from "@/lib/report_api";
import Form from "@/components/form";
import Table from "@/components/table";
import { content } from "@/contents/siteContent";
import SeverityChart from "@/components/severityChart";
import Card from "@/components/card";
import { Report } from "@/components/card";


export default function Home() {

	const [processedReports, setProcessedReports] = useState<Report[]>([]);
	const [historyReports, setHistoryReports] = useState<Report[]>([]);
	const [loading, setLoading] = useState(false);
	const [error, setError] = useState<string | null>(null);

	const handleSubmit = async (formData: ReportForm) => {
		try {
			setLoading(true);
			setError(null);

			const result = await processReport(formData, formData.language || "en");
			setProcessedReports([result]);
			setHistoryReports(prev => [result, ...prev]);
		} catch (err: unknown) {
			if (err instanceof Error) {
				setError(err.message);
			} else {
				setError("Something went wrong");
			}
		}
		finally {
			setLoading(false);
		}
	};


	useEffect(() => {
		getReportHistory().then(setHistoryReports).catch(err => setError(err.message));
	}, []);

	return (
		<div className="home-page">
			<h1>{content.title}</h1>
			<section>
				<div>
					<Form
						fields={content.formFields}
						onSubmit={handleSubmit}
						submitLabel="Process Report"
					/>
					{loading && <p>Processing...</p>}
					{error && <p>{error}</p>}
				</div>

				<div>
					{processedReports.length === 0 &&
						<div className="no-reports">
							<h1>📃</h1>
							<h2> No reports yet</h2>
							<p>Process a report to continue</p>
						</div>}
					{processedReports.map((r, idx) => (
						<Card key={idx} report={r} />
					))}
				</div>
			</section>

			<section>
				<div>
					<h2>History</h2>
					<Table
						columns={content.tableColumns}
						data={historyReports}
					/>
				</div>

				<div>
					<h2>Severity Distribution</h2>
					<SeverityChart data={historyReports} width={500} />
				</div>
			</section>
		</div>
	);
}
