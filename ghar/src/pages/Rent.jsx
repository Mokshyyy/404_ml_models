import React from "react";
import RentCard from "../components/RentCard";
import properties from "../data/properties";
import "../styles/Rent.css";

const Rent = () => {
  const rentProperties = properties.filter(
    (property) => property.type === "Rent"
  );

  return (
    <div className="rent-container">
      <h1>Properties for Rent</h1>
      <div className="rent-grid">
        {rentProperties.map((property) => (
          <RentCard key={property.id} property={property} />
        ))}
      </div>
    </div>
  );
};

export default Rent;
