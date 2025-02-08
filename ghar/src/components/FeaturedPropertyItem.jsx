import React from "react";
import "../styles/home.css";

const FeaturedPropertyItem = ({ data }) => {
  return (
    <div className="property-card">
      <img src={data.image} alt={data.title} />
      <div className="property-info">
        <p>{data.title}</p>
        <p>{data.location}</p>
        <p>{data.price}</p>
      </div>
    </div>
  );
};

export default FeaturedPropertyItem;
