"use client";

import React from "react";
import { BarChart, Bar, XAxis, YAxis, Legend } from "recharts";

export interface Report {
    drug: string;
    adverse_events: string[];
    severity: string;
    outcome: string;
    outcome_translated?: string;
}

interface Props {
    data: Report[];
    width?: number;
    height?: number;
}

const SeverityChart: React.FC<Props> = ({ data, width = 300, height = 500 }) => {
    const counts: Record<string, number> = {};
    data.forEach((report) => {
        const key = report.severity || "Unknown";
        counts[key] = (counts[key] || 0) + 1;
    });

    const chartData = Object.entries(counts).map(([severity, count]) => ({
        severity,
        count,
    }));

    return (
        <BarChart width={width} height={height} data={chartData}>
            <XAxis dataKey="severity" />
            <YAxis allowDecimals={false} />
            <Legend />
            <Bar dataKey="count" fill="#8884d8" />
        </BarChart>
    );
};

export default SeverityChart;
