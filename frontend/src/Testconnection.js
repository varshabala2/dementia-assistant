import React, { useState } from 'react';
import axios from 'axios';

const TestConnection = () => {
    const [message, setMessage] = useState('');

    const testConnection = async () => {
        try {
            const response = await axios.get('http://localhost:5000/api/test');
            setMessage(response.data.message);
        } catch (error) {
            console.error('Error testing connection:', error);
            setMessage('Connection failed!');
        }
    };

    return (
        <div>
            <h2>Test Connection</h2>
            <button onClick={testConnection}>Test Connection</button>
            {message && <p>{message}</p>}
        </div>
    );
};

export default TestConnection;
