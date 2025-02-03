import { Link } from "react-router-dom";
import React from "react";


const BuyCard = ({ property }) => {
  return (
    <div className="buy-property-card">
      <Link to={`/property-details/${property.id}`} className="card-link">
        <div className="buy-property-image-container">
          <img
            src={property.image}
            alt={property.title}
            className="buy-property-image"
          />
        </div>
        <div className="buy-property-details">
          <h3 className="buy-property-title">{property.title}</h3>
          <p className="buy-property-updated">{property.updatedInfo}</p>
          <p className="buy-property-owner">Owner: {property.ownerName}</p>
          <p className="buy-property-owner-expectation">
            Owner Expectation: {property.ownerExpectation}
          </p>
          <p className="buy-property-price">Price: ₹{property.price}</p>
          <p className="buy-property-size">Size: {property.size} sqft</p>
          <p className="buy-property-availability">
            Availability: {property.availability}
          </p>
          <p className="buy-property-deposit">
            Security Deposit: ₹{property.securityDeposit}
          </p>
          <button className="buy-contact-owner-btn">Contact Owner</button>
        </div>
      </Link>
    </div>
  );
};

export default BuyCard;

