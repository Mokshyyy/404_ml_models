import React from "react";
import { useParams } from "react-router-dom";
import properties from "../data/properties";
import PropertyDetails from "../components/PropertyDetails";

const ViewDetails = () => {
  const { id } = useParams();
  const property = properties.find((prop) => prop.id.toString() === id);

  if (!property) {
    return <h2 className="text-center mt-5">Property not found!</h2>;
  }

  return <PropertyDetails property={property} />;
};

export default ViewDetails;
