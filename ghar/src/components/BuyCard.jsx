import { Link } from "react-router-dom";
import React from "react";
import { FaBath, FaBed, FaUser } from "react-icons/fa"; // Icons for bathroom, bedroom, owner

const BuyCard = ({ property }) => {
  return (
    <div className="buy-property-card">
      <Link to={`/property-details/${property.id}`} className="card-link">
        <div className="buy-property-image-container">
          <img
            src={property.image || "/default-property.jpg"} 
            alt={property.title || "Property Image"}
            className="buy-property-image"
          />

        </div>

        <div className="buy-property-details">
          <h3 className="buy-property-title">{property.title}</h3>
          <p className="buy-property-location">{property.location}</p>

          <div className="buy-property-icons">
            <span>
              <FaBed /> {property.rooms} BHK
            </span>
            <span>
              <FaBath /> {property.bathrooms} Bath
            </span>
            <span>
              <FaUser /> {property.ownerExpectation}
            </span>
          </div>

           <div>
              <p className="buy-property-owner">
            <strong>Owner:</strong> {property.ownerName}
          </p>
          <p className="buy-property-price">
            <strong>Price:</strong>
            {(property.price)}
          </p>
          </div>

          <button className="buy-contact-owner-btn">Contact Owner</button>
        </div>
      </Link>
    </div>
  );
};

export default BuyCard;
