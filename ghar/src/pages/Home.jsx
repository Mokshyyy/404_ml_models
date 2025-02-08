import "../styles/home.css";

import React from "react";
import ScrollableSection from "../components/ScrollableSection";
import { brokers } from "../data/brokers";
import { featuredProperties } from "../data/featuredProperties";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();

  const shuffledProperties = [...featuredProperties].sort(() => 0.5 - Math.random()).slice(0, 6);
  const shuffledBrokers = [...brokers].slice(0, 6);

  return (
    <div className="home-container">
      <section className="section">
        <h2>Featured Properties</h2>
        <ScrollableSection items={shuffledProperties} type="property" />
      </section>

      <section className="section">
        <h2>Top Brokers</h2>
        <ScrollableSection items={shuffledBrokers} type="broker" />
      </section>

      {/* Blog Section   loan calculator ko calculate karne ke liye aur naviagte karne ke liye  */}
      <section className="blog-section">
        <div className="blog-card" onClick={() => navigate("/home-loan")}>
          <h3>Predict Your Loan Eligibility</h3>
        </div>
        <div className="blog-card" onClick={() => navigate("/sell")}>
          <h3>Price Prediction in Real Estate</h3>
          <p>Discover how property prices fluctuate and how to predict trends.</p>
        </div>
      </section>
    </div>
  );
};

export default Home;
