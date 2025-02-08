import React from "react";
import { useNavigate } from "react-router-dom";
import BuyCard from "../components/BuyCard";
import properties from "../data/properties";
import "../styles/Buy.css";

const Buy = () => {
  const navigate = useNavigate();

  const buyProperties = properties.filter((property) => property.type === "Buy");

  return (
    <div className="buy-container">



      <button
        className="btn btn-secondary w-100 mt-3"
        onClick={() => navigate("/home-loan")}
      >
        Home Loan Predict
      </button>
       <h1>Properties for sale</h1>
      <div className="buy-list">
        {buyProperties.map((property) => (
          <BuyCard key={property.id} property={property} />
        ))}
      </div>
    </div>
  );
};

export default Buy;
