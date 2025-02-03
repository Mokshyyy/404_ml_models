import React from "react";
import BuyCard from "../components/BuyCard";
import properties from "../data/properties";
import "../styles/Buy.css";

const Buy = () => {
  const buyProperties = properties.filter(
    (property) => property.type === "Buy"
  );

  return (
    <div className="buy-container">
      <h1>Properties for Sale</h1>
      {buyProperties.map((property) => (
        <BuyCard key={property.id} property={property} />
      ))}
    </div>
  );
};

export default Buy;
