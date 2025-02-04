from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Home route
@app.route("/")
def home():
    return render_template('index.html')

# Predict route
@app.route("/predict", methods=["POST"])  # Ensure it accepts POST requests
def predict():
    try:
        # Retrieve data from the form
        data1 = float(request.form['a'])
        data2 = float(request.form['b'])
        data3 = float(request.form['c'])
        data4 = float(request.form['d'])

        # Prepare data for prediction
        arr = np.array([[data1, data2, data3, data4]])

        # Predict
        pred = model.predict(arr)

        # Return prediction to the same page
        return render_template('index.html', prediction=pred[0])
    except Exception as e:
        return f"Error: {e}"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
