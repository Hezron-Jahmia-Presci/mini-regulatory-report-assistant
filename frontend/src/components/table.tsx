"use client";

import React from "react";

export interface Column<T> {
    key: keyof T;
    label: string;
    render?: (value: T[keyof T], row: T) => React.ReactNode;
}

interface Props<T> {
    columns: Column<T>[];
    data: T[];
    maxRows?: number;
    rowHeight?: number;
}

export default function Table<T extends object>({
    columns,
    data,
}: Props<T>) {
    return (
        <div className="table-container">
            <table>
                <thead>
                    <tr>
                        {columns.map((col) => (
                            <th key={String(col.key)}>{col.label}</th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {data.length === 0 && (
                        <tr>
                            <td colSpan={columns.length}>No data available</td>
                        </tr>
                    )}
                    {data.map((row, idx) => (
                        <tr key={idx}>
                            {columns.map((col) => (
                                <td key={String(col.key)}>
                                    {col.render
                                        ? col.render(row[col.key], row)
                                        : (row[col.key] as React.ReactNode)}
                                </td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}
