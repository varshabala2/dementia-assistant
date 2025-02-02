// // import logo from './logo.svg';
// import './App.css';
// import React from 'react';
// import TestConnection from './Testconnection';
import axios from 'axios';
// import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';



// import Home from './pages/Home';
// import Footer from './components/Footer';
// import Navbar from './components/Navbar';
// import Chatbot from './components/Chatbot';


// function App() {
//   return (
//     <div className="app">
//       <Navbar />
//       <div className="main-content"> {/* Pushes footer down */}
//         <Home />
//         <Chatbot />  {/* ✅ Add Chatbot component here */}
//       </div>
//       <Footer />
//     </div>
//   );
// }


// // function App() {
// //   return (
// //     <div className="App">
// //       <Home />
// //     </div>
// //   );
// // }

// export default App;

import './App.css';
import React from 'react';
// import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'; // Import Navigate here

import Home from './pages/Home';
import Footer from './components/Footer';
import Navbar from './components/Navbar';
import Chatbot from './components/Chatbot';
import MedicationForm from './components/MedicationForm'; // Import MedicationForm

function App() {
  return (
    <Router>
      <div className="app">
        <Navbar />
        {/* <Home /> */}
        <div className="main-content">
          <Home /> {/* Home message is now part of the main content */}
          <Routes>
            <Route path="/reminders" element={<MedicationForm />} />
            <Route path="/chat" element={<Chatbot />} />

            {/* <Route path="/" element={<Navigate to="/chat" />} /> Redirect to /chat by default */}
          </Routes>
        </div>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
