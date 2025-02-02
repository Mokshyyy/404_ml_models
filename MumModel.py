# Importing libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib

# Adjusting the plots for better visual
sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

# Reading the dataset
total_df = pd.read_csv("C:/VS Code/Mumbai House Prices.csv")
raw_df = total_df[total_df.type == 'Apartment']

# Convert price to numeric scale
Price_Numeric = {'Cr' : 10000000 , 'L' : 100000}
Price_Order = raw_df.price_unit.map(Price_Numeric)
raw_df['Price_Mag'] = Price_Order * raw_df.price # price magnitude

# Split the dataset for train, validation, and testing
train_val_df, test_df = train_test_split(raw_df, test_size=0.1, random_state=42)
train_df, val_df = train_test_split(train_val_df, test_size=0.25, random_state=42)

# Target Encoding for Region Column
region_target_mean = raw_df.groupby('region')['Price_Mag'].median()

# Apply Target Encoding to the 'region' column
raw_df['region_encoded'] = raw_df['region'].map(region_target_mean)

# Define the function to encode the region
def region_encode(region_name, region_target_mean):
    if region_name in region_target_mean:
        return region_target_mean[region_name]
    else:
        return None  

# Model building and evaluation
model = LinearRegression()
# Apply encoding
train_df['region_encoded'] = train_df['region'].map(region_target_mean)  
# Fitting inputs and target
inputs = train_df[['area', 'bhk', 'region_encoded']] 
targets = train_df['Price_Mag']  
model.fit(inputs, targets)

# Prediction
def predict_price(model, area, bhk, region_name, region_target_mean):
    region_encoded_value = region_encode(region_name, region_target_mean)
    
    if region_encoded_value is None:
        return f"Region '{region_name}' not found in the encoding mapping."
    
    input_data = [[area, bhk, region_encoded_value]]
    
    predicted_price = model.predict(input_data)[0]
    
    return f"Predicted Price for {area} sqft, {bhk} BHK in region '{region_name}': {predicted_price:.2f}"

# Example Prediction
prediction = predict_price(model, 1000, 2, 'Mulund West', region_target_mean)
print(prediction)
