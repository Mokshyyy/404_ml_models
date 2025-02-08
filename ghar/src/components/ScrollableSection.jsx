import React from "react";
import FeaturedPropertyItem from "./FeaturedPropertyItem";
import BrokerCard from "./BrokerCard";
import "../styles/home.css";

const ScrollableSection = ({ items, type }) => {
  return (
    <div className="scroll-container">
      <div className="scroll-content">
        {items.map((item, index) =>
          type === "property" ? (
            <FeaturedPropertyItem key={index} data={item} />
          ) : (
            <BrokerCard key={index} data={item} />
          )
        )}
      </div>
    </div>
  );
};

export default ScrollableSection;
