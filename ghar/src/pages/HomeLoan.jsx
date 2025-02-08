import "../styles/HomeLoan.css"; 

import React, { useState } from "react";

const HomeLoan = () => {
  const [formData, setFormData] = useState({
    applicantIncome: "",
    coapplicantIncome: "",
    loanAmount: "",
    Marriage_Status: "",
    Education_Status: "",
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const { applicantIncome, coapplicantIncome, loanAmount, Marriage_Status, Education_Status } = formData;

    try {
      const response = await fetch(
        `http://127.0.0.1:5000/predict/${applicantIncome}/${coapplicantIncome}/${loanAmount}/${Marriage_Status}/${Education_Status}`
      );
      const data = await response.json();

      setResult(data.Loan_Status === "Y" ? "Loan Approved ✅" : "Loan Rejected ❌");
    } catch (error) {
      setResult("Error: Could not fetch prediction");
    }
  };

  return (
    <div className="loan-container">
      <div className="loan-card">
        <h2>Home Loan Predictor</h2>
        <form onSubmit={handleSubmit}>
          <input type="number" name="applicantIncome" placeholder="Applicant Income" onChange={handleChange} required />
          <input type="number" name="coapplicantIncome" placeholder="Coapplicant Income" onChange={handleChange} required />
          <input type="number" name="loanAmount" placeholder="Loan Amount" onChange={handleChange} required />
          <select name="Marriage_Status" onChange={handleChange} required>
            <option value="">Married?</option>
            <option value="Yes">Yes</option>
            <option value="No">No</option>
          </select>
          <select name="Education_Status" onChange={handleChange} required>
            <option value="">Education</option>
            <option value="Graduate">Graduate</option>
            <option value="Not Graduate">Not Graduate</option>
          </select>
          <button type="submit">Predict</button>
        </form>
        {result && <h3 className="result">{result}</h3>}
      </div>
    </div>
  );
};

export default HomeLoan;
