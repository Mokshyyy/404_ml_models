import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import properties from "../data/properties";
import axios from "axios";
import "../styles/PropertyInfo.css";

const PropertyInfo = () => {
  const { id } = useParams();
  const property = properties.find((prop) => prop.id === parseInt(id));
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    if (!property) return;

    const fetchRecommendations = async () => {
      try {
        const city = property.amenities.find((amenity) =>
          [
            "Gandhinagar",
            "Chandigarh",
            "Patna",
            "Goa",
            "Raipur",
            "Jaipur",
            "Bhopal",
            "Bangalore",
            "Chennai",
            "Hyderabad",
            "Kolkata",
            "Dehradun",
            "New-Delhi",
            "Lucknow",
            "Mumbai",
          ].includes(amenity)
        );

        if (!city) return;

        const tags = property.amenities.join(", ");
        const response = await axios.get(
          `http://127.0.0.1:5000/recommend/${city}/${tags}`
        );

        if (response.data.recommended_properties) {
          setRecommendations(response.data.recommended_properties);
        }
      } catch (error) {
        console.error("Error fetching recommendations:", error);
      }
    };

    fetchRecommendations();
  }, [property]);

  if (!property) return <h2 className="not-found">Property not found</h2>;

  return (
    <div className="property-container">
      <div className="property-details">
        <h1>{property.title}</h1>
        <img
          src={property.image}
          alt={property.title}
          className="property-img"
        />
        <div className="property-info">
          <p>
            <strong>Owner:</strong> {property.ownerName}
          </p>
          <p>
            <strong>Bathrooms:</strong> {property.bathrooms}
          </p>
          <p>
            <strong>Rooms:</strong> {property.rooms}
          </p>
          <p>
            <strong>Availability:</strong> {property.availability}
          </p>
          <p>
            <strong>Price:</strong> {property.price}
          </p>
          <p>
            <strong>Security Deposit:</strong> {property.securityDeposit}
          </p>
          <p>
            <strong>Amenities:</strong> {property.amenities.join(", ")}
          </p>
        </div>
      </div>

      {/* Recommended Properties Section */}
      <h2 className="section-title">Recommended Properties</h2>
      <div className="recommendations">
        {recommendations.length > 0 ? (
          recommendations.map((rec, index) => (
            <div key={index} className="rec-card">
              <p>
                <strong>BHK:</strong> {rec.bhk}
              </p>
              <p>
                <strong>Bathrooms:</strong> {rec.bathrooms}
              </p>
              <p>
                <strong>City:</strong> {rec.city}
              </p>
              <p>
                <strong>Furnishing:</strong> {rec.furnishing}
              </p>
              <p>
                <strong>Amenities:</strong> {rec.amenities.join(", ")}
              </p>
            </div>
          ))
        ) : (
          <p className="no-recommendations">No recommendations available</p>
        )}
      </div>
    </div>
  );
};

export default PropertyInfo;
