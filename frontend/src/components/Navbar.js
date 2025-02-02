

// import React from "react";
// import "./Navbar.css"; // Ensure you have a CSS file for styling

// const Navbar = () => {
//     return (
//         <nav className="navbar">
//             <h1>Mnemo</h1>
//             <ul className="nav-links">
//                 <li><a href="/">Home</a></li>
//                 <li><a href="/reminders">Reminders</a></li>
//                 <li><a href="/chat">Chat</a></li>
//             </ul>
//         </nav>
//     );
// };

// export default Navbar;

import React from "react";
import { Link } from "react-router-dom"; // Import Link for routing
import "./Navbar.css"; // Ensure you have a CSS file for styling

const Navbar = () => {
    return (
        <nav className="navbar">
            <h1>Mnemo</h1>
            <ul className="nav-links">
                <li><Link to="/">Home</Link></li> {/* Use Link instead of <a> */}
                <li><Link to="/reminders">Reminders</Link></li> {/* Use Link instead of <a> */}
                <li><Link to="/chat">Chat</Link></li> {/* Use Link instead of <a> */}
            </ul>
        </nav>
    );
};

export default Navbar;
