from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np

# Load the trained model and encoding data (you should save these from your existing script)
model = pickle.load(open("model.pkl", "rb"))
loc_mean = pickle.load(open("loc_mean.pkl", "rb"))

# Initialize Flask app
app = Flask(__name__)

# Define a function to encode the region
def region_encode(region_name, loc_mean):
    if region_name in loc_mean:
        return loc_mean[region_name]
    else:
        return None
    
@app.route('/')  # This adds a homepage route
def home():
    return jsonify({"message": "Welcome to the House Price Prediction API!"})

# Define prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get data from the frontend
    area = data.get('area')
    bhk = data.get('bhk')
    bath = data.get('bath')
    balcony = data.get('balcony')
    region_name = data.get('region')
    
    region_encoded_value = region_encode(region_name, loc_mean)
    
    if region_encoded_value is None:
        return jsonify({'error': f"Region '{region_name}' not found in the encoding mapping."}), 400
    
    input_data = [[area, bhk, bath, balcony, region_encoded_value]]
    predicted_price = model.predict(input_data)[0]
    
    return jsonify({'predicted_price': round(predicted_price, 2)})

if __name__ == '__main__':
    app.run(debug=True)
