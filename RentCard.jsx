import "../styles/Rent.css"; 

import { FaBath, FaBed, FaUser } from "react-icons/fa";

import React from "react";
import { useNavigate } from "react-router-dom";

const RentCard = ({ property }) => {
  const navigate = useNavigate();

  return (
    <div className="rent-card" onClick={() => navigate(`/property/${property.id}`)}>
      <img src={property.image} alt={property.title} className="rent-image" />
      <div className="rent-details">
        <div className="rent-info">
          <span><FaBed /> {property.rooms} BHK</span>
          <span><FaBath /> {property.bathrooms} Bath</span>
        </div>
        <div className="rent-owner">
          <FaUser /> <span>{property.owner}</span>
        </div>
        <div className="rent-price">₹{property.price.toLocaleString()}</div>
      </div>
    </div>
  );
};

export default RentCard;
