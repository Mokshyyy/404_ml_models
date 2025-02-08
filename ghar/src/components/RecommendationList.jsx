// import "../styles/RecommendationList.css";

// import React from "react";
// import { useNavigate } from "react-router-dom";

// const RecommendationList = ({ recommendations, onCardClick }) => {
//   const navigate = useNavigate();

//   return (
//     <div className="recommendation-list">
//       <h2>Recommended Properties</h2>
//       <div className="recommendation-container">
//         {recommendations.length > 0 ? (body {
//   bbody {
//   background-image: url("img_tree.gif"), url("paper.gif");
//   background-color: #cccccc;
// }
//           recommendations.map((property) => (
//             <div
//               key={property.id}
//               className="recommendation-card"
//               onClick={() => {
//                 if (onCardClick) {
//                   onCardClick(property.id);
//                 } else {
//                   navigate(`/property/${property.id}`);
//                 }
//               }}
//             >
//               <img src={property.image} alt={property.title} />
//               <h3>{property.title}</h3>
//               <p>Price: {property.price}</p>
//             </div>
//           ))
//         ) : (
//           <p>No recommendations available</p>
//         )}
//       </div>
//     </div>
//   );
// };

// export default RecommendationList;
