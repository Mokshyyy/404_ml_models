import React from "react";
import "../styles/home.css";

const BrokerCard = ({ data }) => {
  return (
    <div className="broker-card">
      <img src={data.image} alt={data.name} />
      <div className="broker-info">
        <h3>{data.name}</h3>
        <p>{data.contact}</p>
      </div>
    </div>
  );
};

export default BrokerCard;
