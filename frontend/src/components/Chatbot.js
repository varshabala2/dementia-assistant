import React, { useState, useEffect } from "react";
import axios from "axios";
import "./Chatbot.css"; // Ensure you have the CSS file for styling

const Chatbox = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");

    useEffect(() => {
        // AI's initial greeting message
        setMessages([{ sender: "ai", text: "Hi! I am Mnemo, your AI assistant. What can I help you with?" }]);
    }, []);

    const sendMessage = async () => {
        if (!input.trim()) return;

        const userMessage = { sender: "user", text: input };
        setMessages((prev) => [...prev, userMessage]); // Add user message to chat

        try {
            const response = await axios.post("http://localhost:5000/chat_with_ai", {
                message: input,
            });

            const aiMessage = { sender: "ai", text: response.data.reply };
            setMessages((prev) => [...prev, aiMessage]); // Add AI response to chat
        } catch (error) {
            console.error("Error communicating with AI:", error);
        }

        setInput(""); // Clear input field
    };

    return (
        <div className="chat-container">
            <div className="chatbox">
                {messages.map((msg, index) => (
                    <div key={index} className={`message ${msg.sender}`}>
                        {msg.text}
                    </div>
                ))}
            </div>

            <div className="input-container">
                <input
                    type="text"
                    placeholder="Type a message..."
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={(e) => e.key === "Enter" && sendMessage()}
                />
                <button onClick={sendMessage}>Send</button>
            </div>
        </div>
    );
};

export default Chatbox;
