import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import  "../styles/sell.css";
const Sell = () => {
  const navigate = useNavigate();
  const [city, setCity] = useState("delhi");
  const [area, setArea] = useState("");
  const [bedrooms, setBedrooms] = useState("");
  const [bathrooms, setBathrooms] = useState("");
  const [predictedPrice, setPredictedPrice] = useState(null);
  const [error, setError] = useState("");

  const handlePredict = async () => {
    if (!area || !bedrooms || (city !== "mumbai" && !bathrooms)) {
      setError("Please fill all fields");
      return;
    }
    setError("");

    try {
      const url =
        city === "mumbai"
          ? `http://127.0.0.1:5000/prediction/${city}/${area}/${bedrooms}/0`
          : `http://127.0.0.1:5000/prediction/${city}/${area}/${bedrooms}/${bathrooms}`;

      const response = await fetch(url);
      const data = await response.json();
      setPredictedPrice(data.predicted_price);
    } catch (err) {
      console.error("Error fetching prediction:", err);
      setError("Failed to get prediction. Check backend.");
    }
  };

  return (
    <div className="container mt-5  sell-container">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <div className="card shadow p-4">
            <h2 className="text-center">Sell Your Property</h2>
            <p className="text-muted text-center">
              Use our AI-powered tool to estimate the price of your property.
            </p>

            {/* City Selection */}
            <div className="mb-3">
              <label className="form-label">City:</label>
              <select
                className="form-select"
                value={city}
                onChange={(e) => setCity(e.target.value)}
              >
                <option value="delhi">Delhi</option>
                <option value="bangalore">Bangalore</option>
                <option value="mumbai">Mumbai</option>
              </select>
            </div>

            {/* Area Input */}
            <div className="mb-3">
              <label className="form-label">Area (sqft):</label>
              <input
                type="number"
                className="form-control"
                value={area}
                onChange={(e) => setArea(e.target.value)}
                placeholder="Enter area in sqft"
              />
            </div>

            {/* Bedrooms Input */}
            <div className="mb-3">
              <label className="form-label">Bedrooms:</label>
              <input
                type="number"
                className="form-control"
                value={bedrooms}
                onChange={(e) => setBedrooms(e.target.value)}
                placeholder="Number of bedrooms"
              />
            </div>

            {/* Bathrooms Input (Hidden for Mumbai) */}
            {city !== "mumbai" && (
              <div className="mb-3">
                <label className="form-label">Bathrooms:</label>
                <input
                  type="number"
                  className="form-control"
                  value={bathrooms}
                  onChange={(e) => setBathrooms(e.target.value)}
                  placeholder="Number of bathrooms"
                />
              </div>
            )}

            {/* Predict Price Button */}
            <button className="btn btn-primary w-100" onClick={handlePredict}>
              Predict Price
            </button>



            {/* Error Message */}
            {error && <p className="text-danger mt-3">{error}</p>}

            {/* Prediction Result */}
            {predictedPrice !== null && (
              <p className="text-success mt-3">
                <strong>Predicted Price: ₹{predictedPrice} Lakhs</strong>
              </p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Sell;
