// Chatbot.js
import React, { useState } from 'react';

const Chatbot = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');

    const sendMessage = () => {
        if (input.trim() !== '') {
            setMessages([...messages, { text: input, sender: 'User' }]);
            setInput('');
            setTimeout(() => {
                setMessages(prevMessages => [...prevMessages, { text: "I'm here to help!", sender: 'AI' }]);
            }, 1000);
        }
    };

    return (
        <div className="p-4 border rounded-lg shadow-lg w-full">
            <h2 className="text-xl font-semibold mb-2">Chatbot</h2>
            <div className="border p-2 h-40 overflow-y-auto mb-2">
                {messages.map((msg, index) => (
                    <p key={index} className={msg.sender === 'User' ? 'text-right' : 'text-left'}>
                        <strong>{msg.sender}:</strong> {msg.text}
                    </p>
                ))}
            </div>
            <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Type a message..."
                className="border p-2 rounded w-full mb-2"
            />
            <button onClick={sendMessage} className="bg-green-500 text-white px-4 py-2 rounded">
                Send
            </button>
        </div>
    );
};

export default Chatbot;