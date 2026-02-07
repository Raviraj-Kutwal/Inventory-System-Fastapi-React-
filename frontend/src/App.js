import React from "react";
import { BrowserRouter as Router, Routes, Route, Link, useLocation } from "react-router-dom";
import "./App.css";
import Inventory from "./components/Inventory";
import Dashboard from "./components/Dashboard";

// Navigation Component to handle active states
function Navigation() {
  const location = useLocation();
  const isActive = (path) => location.pathname === path ? "nav-link active" : "nav-link";

  return (
    <nav className="top-nav">
      <Link to="/" className={isActive("/")}>Inventory</Link>
      <Link to="/dashboard" className={isActive("/dashboard")}>Dashboard</Link>
    </nav>
  );
}

function App() {
  return (
    <Router>
      <div className="app-bg">
        <header className="topbar">
          <div className="brand">
            <span className="brand-badge">📦</span>
            <h1>Telusko Trac</h1>
          </div>
          <Navigation />
        </header>

        <Routes>
          <Route path="/" element={<Inventory />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
