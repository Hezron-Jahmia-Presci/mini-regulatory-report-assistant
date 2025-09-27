"use client";

import React from "react";

export interface Report {
    drug: string;
    adverse_events: string[];
    severity: string;
    outcome: string;
    outcome_translated?: string;
    doctor?: string;
    report?: string;
}

interface Props {
    report: Report;
}

export default function Card({ report }: Props) {
    return (
        <div className="card">
            <h3><strong>Drug:</strong> {report.drug}</h3>

            <section>
                <div>
                    <strong>Doctor:</strong>
                    <strong>Adverse Events:</strong>{" "}
                    <strong>Severity:</strong>
                    <strong>Outcome:</strong>
                    <strong>Translated Outcome:</strong>
                </div>

                <div>
                    <p>{report.doctor || "Unknown"}</p>
                    <p> {report.adverse_events && report.adverse_events.length > 0
                        ? report.adverse_events.join(", ")
                        : "None"}</p>
                    <p>{report.severity}</p>
                    <p>{report.outcome}</p>
                    <p> {report.outcome_translated && report.outcome_translated !== report.outcome
                        ? report.outcome_translated
                        : "N/A"}</p>
                </div>
            </section>
        </div>
    );
}
