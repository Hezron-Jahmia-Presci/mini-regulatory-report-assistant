"use client"

import { useState } from 'react'

export interface Field {
    name: string
    label: string
    type: 'text' | 'textarea' | 'number' | 'select'
    placeholder?: string
    options?: string[]
    required?: boolean
}

interface Props<T extends Record<string, string | number>> {
    fields: Field[]
    onSubmit: (data: T) => void | Promise<void>
    submitLabel?: string
}

export default function Form<T extends Record<string, string | number>>({
    fields,
    onSubmit,
    submitLabel = 'Submit'
}: Props<T>) {
    // Initialize form state
    const initialState = {} as T
    fields.forEach(f => {
        if (f.type === 'select') {
            initialState[f.name as keyof T] = (f.options?.[0] ?? '') as T[keyof T]
        } else if (f.type === 'number') {
            initialState[f.name as keyof T] = 0 as T[keyof T]
        } else {
            initialState[f.name as keyof T] = '' as T[keyof T]
        }
    })

    const [formData, setFormData] = useState<T>(initialState)

    const handleChange = (name: keyof T, value: string) => {
        const field = fields.find(f => f.name === name)
        if (!field) return

        let parsedValue: string | number = value
        if (field.type === 'number') {
            parsedValue = Number(value)
        }

        setFormData(prev => ({ ...prev, [name]: parsedValue } as T))
    }

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault()
        onSubmit(formData)
    }

    return (
        <form onSubmit={handleSubmit}>
            {fields.map(f => (
                <div key={f.name}>
                    <label htmlFor={f.name}>{f.label}</label>

                    {f.type === 'textarea' ? (
                        <textarea
                            id={f.name}
                            placeholder={f.placeholder}
                            value={formData[f.name as keyof T]}
                            onChange={e => handleChange(f.name as keyof T, e.target.value)}
                        />
                    ) : f.type === 'select' ? (
                        <select
                            id={f.name}
                            value={formData[f.name as keyof T]}
                            onChange={e => handleChange(f.name as keyof T, e.target.value)}
                        >
                            {f.options?.map(opt => (
                                <option key={opt} value={opt}>{opt}</option>
                            ))}
                        </select>
                    ) : (
                        <input
                            type={f.type}
                            id={f.name}
                            placeholder={f.placeholder}
                            value={formData[f.name as keyof T]}
                            onChange={e => handleChange(f.name as keyof T, e.target.value)}
                        />
                    )}
                </div>
            ))}
            <button type="submit">{submitLabel}</button>
        </form>
    )
}
