import React from 'react';

const Footer = () => {
    return (
        <footer className="p-4 bg-gray-800 text-white text-center mt-6">
            <p>&copy; {new Date().getFullYear()} Mnemo. All rights reserved.</p>
        </footer>
    );
};

export default Footer;
