#importing lib
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
#cities for diff models
MODEL_CITY = {
    "delhi": "del_model.pkl",
    "bangalore": "bang_model.pkl",
    "mumbai" : "mum_model.pkl"
}
RECOMMENDATION_CITIES = {
    "gandhinagar", "chandigarh", "patna", "goa", "raipur", "jaipur", 
    "bhopal", "bangalore", "chennai", "hyderabad", "kolkata", "dehradun", 
    "new-delhi", "lucknow", "mumbai"
}
#mapping for bool 
MARRIED_MAP = {"No": 0, "Yes": 1}
EDUCATION_MAP = {"Graduate": 1, "Not Graduate": 0}
#deployment of price prediciton models
class Prediction(Resource):
    def get(self,city, area, bedrooms, bathrooms):
        if city.lower() not in MODEL_CITY:
            return jsonify({"error": "City model not available"})
        
        print(f"Received area: {area}, bedrooms: {bedrooms}, bathrooms: {bathrooms}")

        #diffrent input for diffrent cities
        if city.lower() == "mumbai":
            input_data = np.array([[int(area),int(bedrooms)]])
        else :
            input_data = np.array([[int(area), int(bedrooms), int(bathrooms)]])

        # Load the model
        model_path = MODEL_CITY[city.lower()]
        with open(model_path, "rb") as f:
            model = pickle.load(f)

        # Perform prediction
        prediction = model.predict(input_data)
        prediction = float(prediction[0])  # Convert to integer

        # Return JSON response
        return jsonify({"predicted_price": prediction})
#deployment for recommendations
class Recommendation(Resource):
    def get(self, city, tags):
        if city.lower() not in RECOMMENDATION_CITIES:
            return jsonify({"error": "City not available for recommendations"})

        print(f"Received tags for recommendation: {tags}")

        # Load dataset
        df = pd.read_csv('Scraped_Data.csv')
        df = df.replace(9, None) 
        df = df.replace("9",None)
        # Selecting necessary columns for inputs
        rec_df = df[['propertyType', 'furnishing', 'city', 'bedrooms', 'bathrooms',
                     'Swimming_Pool', 'Reserved_Parking', 'Club_House', 'Gymnasium',
                     'Kids_Play_Area', 'Park', 'Bank__And__ATM']].dropna()

        # Convert numerical values to readable tags
        def format_bhk(n): return f"{int(n)} bhk"
        def format_bath(n): return f"{int(n)} bathrooms"
        def amenity_tag(value, tag_name): return tag_name if value == 1 else ""
        #formatting all tags
        rec_df['BHK'] = rec_df['bedrooms'].apply(format_bhk)
        rec_df['bath'] = rec_df['bathrooms'].apply(format_bath)
        rec_df['SP'] = rec_df['Swimming_Pool'].apply(lambda x: amenity_tag(x, "Swimming Pool"))
        rec_df['RP'] = rec_df['Reserved_Parking'].apply(lambda x: amenity_tag(x, "Reserved Parking"))
        rec_df['CH'] = rec_df['Club_House'].apply(lambda x: amenity_tag(x, "Club House"))
        rec_df['Gym'] = rec_df['Gymnasium'].apply(lambda x: amenity_tag(x, "Gym"))
        rec_df['KPA'] = rec_df['Kids_Play_Area'].apply(lambda x: amenity_tag(x, "Kids Play Area"))
        rec_df['P'] = rec_df['Park'].apply(lambda x: amenity_tag(x, "Park"))
        rec_df['A'] = rec_df['Bank__And__ATM'].apply(lambda x: amenity_tag(x, "ATM"))

        # Creating a combined "tags" column for recommendations
        rec_df['tags'] = rec_df[['propertyType', 'furnishing', 'city', 'BHK', 'bath', 'SP', 'RP', 'CH', 'Gym', 'KPA', 'P', 'A']].agg(', '.join, axis=1)

        # model building and training
        Tfidf_Vectorizer = TfidfVectorizer()
        vector_matrix = Tfidf_Vectorizer.fit_transform(rec_df['tags'])
        input_vector = Tfidf_Vectorizer.transform([tags])  
        rec_sys = cosine_similarity(input_vector, vector_matrix)

        # Get the indices of the top 5 most similar properties
        top_indices = rec_sys.argsort()[0][-5:][::-1]

        # Prepare structured response
        recommended_properties = []
        for idx in top_indices:
            recommended_properties.append({
                "bhk": rec_df.iloc[idx]['BHK'],  # FIXED: Correct column name
                "bathrooms": rec_df.iloc[idx]['bath'],  # FIXED: Correct column name
                "city": rec_df.iloc[idx]['city'],
                "furnishing": rec_df.iloc[idx]['furnishing'],
                "amenities": [tag for tag in [
                    rec_df.iloc[idx]['SP'], rec_df.iloc[idx]['RP'], rec_df.iloc[idx]['CH'],
                    rec_df.iloc[idx]['Gym'], rec_df.iloc[idx]['KPA'], rec_df.iloc[idx]['P'], rec_df.iloc[idx]['A']
                ] if tag]  # Filtering out empty values
            })

        return jsonify({"recommended_properties": recommended_properties})
#loading model for loan predict       
with open("Loan_pred.pkl","rb") as f:
    model = pickle.load(f)
#model for loan predict
class LoanPredict(Resource):
    def get(self,applicant_income,coapplicant_income,loan_amount,Marriage_Status,Education_Status):
        try:
            
            applicant_income = int(applicant_income)
            coapplicant_income = int(coapplicant_income)
            loan_amount = int(loan_amount)
        
            MARRIED_MAP = {"No": 0, "Yes": 1}
            EDUCATION_MAP = {"Graduate": 1, "Not Graduate": 0}

            married = MARRIED_MAP.get(Marriage_Status.strip(), 0)
            education = EDUCATION_MAP.get(Education_Status.strip(),1)
            
            input_data = np.array([[applicant_income, coapplicant_income, loan_amount, married, education]])
            prediction = model.predict(input_data)[0]

            return jsonify({"Loan_Status": prediction})

        except Exception as e:
            return jsonify({"error": str(e)})
    
# API routes
api.add_resource(Prediction,'/prediction/<string:city>/<int:area>/<int:bedrooms>/<int:bathrooms>')
api.add_resource(Recommendation, "/recommendation/<string:city>/<string:tags>")
api.add_resource(LoanPredict, "/predict/<int:applicant_income>/<int:coapplicant_income>/<int:loan_amount>/<string:Marriage_Status>/<string:Education_Status>")

if __name__ == '__main__':
    app.run(debug=True)


