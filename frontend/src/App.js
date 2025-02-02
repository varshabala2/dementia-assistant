// import logo from './logo.svg';
import './App.css';
import React from 'react';
import TestConnection from './Testconnection';

import Home from './pages/Home';
import Footer from './components/Footer';
import Navbar from './components/Navbar';
import Chatbot from './components/Chatbot';


function App() {
  return (
    <div className="app">
      <Navbar />
      <div className="main-content"> {/* Pushes footer down */}
        <Home />
        <Chatbot />  {/* ✅ Add Chatbot component here */}
      </div>
      <Footer />
    </div>
  );
}


// function App() {
//   return (
//     <div className="App">
//       <Home />
//     </div>
//   );
// }

export default App;
// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//         <p>Hello, World!</p> {/* Added this line */}
//         <TestConnection /> {/* Added this line */}
//       </header>
//     </div>
//   );
// }

// export default App;
