from flask import Flask, jsonify
from flask_restful import Resource, Api
import pickle
import numpy as np
from flask_cors import CORS
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

app = Flask(__name__)
api = Api(app)
CORS(app) 
MODEL_PATHS = {
    "delhi": "del_model.pkl",
    "bangalore": "bang_model.pkl",
    "mumbai" : "mum_model.pkl"
}
RECOMMENDATION_CITIES = {
    "gandhinagar", "chandigarh", "patna", "goa", "raipur", "jaipur", 
    "bhopal", "bangalore", "chennai", "hyderabad", "kolkata", "dehradun", 
    "new-delhi", "lucknow", "mumbai"
}
class Prediction(Resource):
    def get(self,city, area, bedrooms, bathrooms):
        if city.lower() not in MODEL_PATHS:
            return jsonify({"error": "City model not available"})
        
        print(f"Received area: {area}, bedrooms: {bedrooms}, bathrooms: {bathrooms}")

        #diffrent input for diffrent cities
        if city.lower() == "mumbai":
            input_data = np.array([[int(area),int(bedrooms)]])
        else :
            input_data = np.array([[int(area), int(bedrooms), int(bathrooms)]])

        # Load the model
        model_path = MODEL_PATHS[city.lower()]
        with open(model_path, "rb") as f:
            model = pickle.load(f)

        # Perform prediction
        prediction = model.predict(input_data)
        prediction = float(prediction[0])  # Convert to integer

        # Return JSON response
        return jsonify({"predicted_price": prediction})
class Recommendation(Resource):
    def get(self, city, tags):
        if city.lower() not in RECOMMENDATION_CITIES:
            return jsonify({"error": "City not available for recommendations"})

        print(f"Received tags for recommendation: {tags}")
        df = pd.read_csv('Scraped_Data.csv')
        df= df.replace("9",None)
        df = df.replace(9,None)
        #selecting coloumns for model
        rec_df = df[['propertyType','furnishing','carpetAreaUnit','bedrooms','city','bathrooms','balconies','Swimming_Pool','Reserved_Parking','Club_House','Gymnasium','Kids_Play_Area','Park','Bank__And__ATM']].dropna()
        #integer to tags
        def BHK(n):
            return str(n) + " bhk" 
        def bath(n):
            return str(n) + " bathrooms"
        def balcony(n):
            return str(n) + " balcony"
        def amenity_tag(value, tag_name):
            return tag_name if value == 1 else ""
        #boolean to tags
        rec_df['BHK'] = rec_df['bedrooms'].apply(BHK)
        rec_df['bath'] = rec_df['bathrooms'].apply(bath)
        rec_df['balcony'] = rec_df['balconies'].apply(balcony)
        rec_df['SP'] = rec_df['Swimming_Pool'].apply(lambda x: amenity_tag(x, "Swimming Pool"))
        rec_df['RP'] = rec_df['Reserved_Parking'].apply(lambda x: amenity_tag(x, "Reserved Parking"))
        rec_df['CH'] = rec_df['Club_House'].apply(lambda x: amenity_tag(x, "Club House"))
        rec_df['Gym'] = rec_df['Gymnasium'].apply(lambda x: amenity_tag(x, "Gym"))
        rec_df['KPA'] = rec_df['Kids_Play_Area'].apply(lambda x: amenity_tag(x, "Kids Play Area"))
        rec_df['P'] = rec_df['Park'].apply(lambda x: amenity_tag(x, "Park"))
        rec_df['A'] = rec_df['Bank__And__ATM'].apply(lambda x: amenity_tag(x, "ATM"))
        rec_df['tags'] = rec_df[['propertyType', 'furnishing' ,'BHK','bath','balcony','SP','RP','CH','Gym','KPA','P','A']].agg(', '.join, axis=1)
        
        # print(rec_df.tags)
        Tfidf_Vectorizer = TfidfVectorizer()
        vector_matrix = Tfidf_Vectorizer.fit_transform(rec_df['tags'])
        input_tag = [tags]  # Tags passed by the user
        input_vector = Tfidf_Vectorizer.transform(input_tag) 
        # Calculate cosine similarity between the input tag and the dataset
        rec_sys = cosine_similarity(input_vector, vector_matrix)

        # Get the indices of the top 5 most similar properties
        top_indices = rec_sys.argsort()[0][-5:][::-1]
        
        # Fetch the corresponding tags for the top 5 similar properties
        recommended_properties = []
        for idx in top_indices:
            recommended_properties.append(rec_df.iloc[idx]['tags'])

        # Return the tags of the top 5 recommended properties
        return jsonify({"recommended_properties": recommended_properties})
    
# Define the API route
api.add_resource(Prediction,'/prediction/<string:city>/<int:area>/<int:bedrooms>/<int:bathrooms>')
api.add_resource(Recommendation, '/recommendation/<string:city>/<tags>')

if __name__ == '__main__':
    app.run(debug=True)

