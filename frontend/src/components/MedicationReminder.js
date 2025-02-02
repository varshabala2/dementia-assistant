import React, { useState } from 'react';

const MedicationReminder = () => {
    const [reminders, setReminders] = useState([]);
    const [newReminder, setNewReminder] = useState('');

    const addReminder = () => {
        if (newReminder.trim() !== '') {
            setReminders([...reminders, newReminder]);
            setNewReminder('');
        }
    };

    return (
        <div className="p-4 border rounded-lg shadow-lg w-full">
            <h2 className="text-xl font-semibold mb-2">Medication Reminders</h2>
            <input
                type="text"
                value={newReminder}
                onChange={(e) => setNewReminder(e.target.value)}
                placeholder="Enter reminder..."
                className="border p-2 rounded w-full mb-2"
            />
            <button onClick={addReminder} className="bg-blue-500 text-white px-4 py-2 rounded">
                Add Reminder
            </button>
            <ul className="mt-2">
                {reminders.map((reminder, index) => (
                    <li key={index} className="p-2 border-b">{reminder}</li>
                ))}
            </ul>
        </div>
    );
};

export default MedicationReminder;