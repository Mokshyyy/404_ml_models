import React, { useEffect, useState } from "react";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";

import Buy from "./pages/Buy";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import HomeLoan from "./pages/HomeLoan";
import Navbar from "./components/Navbar";
import PropertyDetails from "./components/PropertyDetails"
import PropertyInfo from "./pages/PropertyInfo";
import PropertyPage from "./pages/PropertyPage";
import Rent from "./pages/Rent";
import Sell from "./pages/Sell";
import ViewDetails from "./pages/ViewDetails";

const App = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5000/login-status", {
          credentials: "include",
        });
        const data = await response.json();
        if (data.user) setUser(data.user);
      } catch (error) {
        console.error("Error fetching user:", error);
      }
    };

    fetchUser();
  }, []);

  return (
    <Router>
      <Navbar user={user} setUser={setUser} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/rent" element={<Rent />} />
        <Route path="/buy" element={<Buy />} />
        <Route path="/sell" element={<Sell />} />
        <Route path="/property-details/:id" element={<PropertyInfo />} />
        <Route path="/property/:id/details" element={<PropertyDetails />} />
        <Route path="/view/:id" element={<ViewDetails />} />
        <Route path="/property/:id" element={<PropertyPage />} />
        <Route path="/home-loan" element={<HomeLoan />} />
      </Routes>
      <Footer />
    </Router>
  );
};

export default App;
