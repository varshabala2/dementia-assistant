
// // export default Navbar;
// import React from 'react';

// const Navbar = () => {
//     return (
//         <nav className="p-4 bg-gray-800 text-white w-full text-center">
//             <h2 className="text-lg font-semibold">Dementia Assistant</h2>
//             <ul className="flex justify-center space-x-4 mt-2">
//                 <li><a href="/" className="hover:underline">Home</a></li>
//                 <li><a href="/reminders" className="hover:underline">Reminders</a></li>
//                 <li><a href="/chat" className="hover:underline">Chat</a></li>
//             </ul>
//         </nav>
//     );
// };

// export default Navbar;

import React from "react";
import "./Navbar.css"; // Ensure you have a CSS file for styling

const Navbar = () => {
    return (
        <nav className="navbar">
            <h1>Mnemo</h1>
            <ul className="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/reminders">Reminders</a></li>
                <li><a href="/chat">Chat</a></li>
            </ul>
        </nav>
    );
};

export default Navbar;

