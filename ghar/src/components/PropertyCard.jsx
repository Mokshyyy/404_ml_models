import { FaBath, FaBed, FaUser } from "react-icons/fa"; // Importing Icons

import React from "react";
import { useNavigate } from "react-router-dom"; // For navigating to Property Details page

const PropertyCard = ({ property }) => {
  const navigate = useNavigate();

  const handleClick = () => {

    navigate(`/property/${property.id}`);
  };

  return (
    <div className="property-card" onClick={handleClick}>
      <div className="property-image-container">
        <img
          src={property.image}
          alt={property.title}
          className="property-image"
        />
      </div>

      <div className="property-details">
        <div className="property-info">
          <h3>{property.title}</h3>
          <div className="details">
            <span><FaBed /> {property.rooms} BHK</span>
            <span><FaBath /> {property.bathrooms} Bath</span>
          </div>
        </div>

        <div className="owner-details">
          <FaUser /> <span>{property.owner}</span>
          <p>Contact: {property.contact}</p>
        </div>

        <div className="property-price">
          {property.price.toLocaleString()}
        </div>
      </div>
    </div>
  );
};

export default PropertyCard;

