import { useParams } from "react-router-dom";
import properties from "../data/properties";

const PropertyDetails = () => {
  const { id } = useParams();
  const property = properties.find((prop) => prop.id === parseInt(id));

  if (!property) {
    return <h2 className="text-center mt-5">Property not found</h2>;
  }

  return (
    <div className="container mt-5 pt-5">
      <h2>{property.title}</h2>
      <img
        src={property.image}
        alt={property.title}
        className="img-fluid mb-3"
      />
      <p>{property.description}</p>
      <p><strong>Price:</strong> ₹{property.price}</p>
      <p><strong>Owner:</strong> {property.ownerName}</p>
      <p><strong>Contact:</strong> {property.contact}</p>
    </div>
  );
};

export default PropertyDetails;
