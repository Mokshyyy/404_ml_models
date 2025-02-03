import "./styles/App.css";
import "@fortawesome/fontawesome-free/css/all.min.css";

import { Route, BrowserRouter as Router, Routes } from "react-router-dom";

import Buy from "./pages/Buy";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import Navbar from "./components/Navbar";
import PropertyDetails from "./components/PropertyDetails"; 
import React from "react";
import Rent from "./pages/Rent";
import ViewDetails from "./pages/ViewDetails";

const App = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/rent" element={<Rent />} />
        <Route path="/buy" element={<Buy />} />
        <Route path="/view/:id" element={<ViewDetails />} />
        <Route path="/property/:id" element={<PropertyDetails />} />
      </Routes>
      <Footer />
    </Router>
  );
};

export default App;
