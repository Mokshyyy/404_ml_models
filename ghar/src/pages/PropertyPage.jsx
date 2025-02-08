import React from "react";
import { Routes, Route } from "react-router-dom";
import PropertyInfo from "./PropertyInfo";

const PropertyPage = () => {
  return (
    <Routes>
      <Route path="/property/:id" element={<PropertyInfo />} />
    </Routes>
  );
};

export default PropertyPage;
