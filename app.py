from flask import Flask, jsonify
from flask_restful import Resource, Api
import pickle
import numpy as np

app = Flask(__name__)
api = Api(app)

class Prediction(Resource):
    def get(self, area, bedrooms, bathrooms, neworold):
        print(f"Received area: {area}, bedrooms: {bedrooms}, bathrooms: {bathrooms}")

        # Prepare the input as a 2D numpy array
        input_data = np.array([[int(area), int(bedrooms), int(bathrooms)]])

        # Load the model
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)

        # Perform prediction
        prediction = model.predict(input_data)
        prediction = int(prediction[0])  # Convert to integer

        # Return JSON response
        return jsonify({"predicted_price": prediction})

# Define the API route
api.add_resource(Prediction, '/prediction/<int:area>/<int:bedrooms>/<int:bathrooms>')

if __name__ == '__main__':
    app.run(debug=True)
