import { Field } from "@/components/form"
import { Column } from "@/components/table"
import { Report } from "@/components/card"

export const content = {
    title: "Mini Regulatory Report Assistant",

    formFields: [
        { name: 'report', label: 'Medical Report', type: 'textarea', placeholder: 'Paste your report' },
        { name: 'doctor', label: 'Doctor Name', type: 'text', placeholder: 'Enter doctor name' },
        {
            name: 'language',
            label: 'Language',
            type: 'select',
            options: ['en', 'fr', 'sw']  // English, French, Swahili
        },
    ] as Field[],

    tableColumns: [
        { key: "drug", label: "Drug Name" },
        {
            key: "adverse_events",
            label: "Adverse Events",
            render: (value: string[]) => value.join(", "),
        },
        { key: "severity", label: "Severity" },
        { key: "outcome", label: "Outcome" },
        // { key: "outcome_translated", label: "Translated Outcome" },
        // { key: "doctor", label: "Doctor" },
    ] as Column<Report>[],
}
