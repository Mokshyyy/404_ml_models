import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
import plotly.express as px
import matplotlib
import numpy as np
import re
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
# making dataframes
raw_df = pd.read_csv('bengaluru_house_prices.csv')
total_df = raw_df.dropna().copy(0)
train_df, val_df = train_test_split(total_df, test_size=0.1)

 #  Adjusting size coloumn for numeric values
total_df.loc[:, 'bhk'] = total_df["size"].apply(lambda x: int(x.split(" ")[0]))

# adjusting area coloumn
def convert_sqft_to_number(x):
    tokens = x.split("-")
    if len(tokens) == 2:
        return (float(tokens[0])+float(tokens[1]))/2
    try:
        return float(x)
    except:
        return None
    
# Remove rows where 'total_sqft' has non-numeric values (units included)
total_df = total_df[total_df["total_sqft"].str.isnumeric()]

# grouping location with less frequency
loc_fre = total_df['location'].value_counts()
total_df['loca'] = total_df['location'].apply(lambda x : x if loc_fre[x] >= 10 else 'other')

# grouping/encoding by mean of location prices
loc_mean = total_df.groupby('loca')['price'].median()
total_df['region_encoded'] = total_df['loca'].map(loc_mean)

# Convert the column to numeric
total_df["total_sqft"] = pd.to_numeric(total_df["total_sqft"])
total_df = total_df[(total_df["total_sqft"] <= 30000)]

# Define the function to encode the region
def region_encode(region_name, loc_mean):
    if region_name in loc_mean:
        return loc_mean[region_name]
    else:
        return None  
print(total_df.price.corr(total_df.bhk))
#Model building
model = LinearRegression()
inputs = total_df[['total_sqft','bhk','bath']]
target = total_df['price']
model.fit(inputs,target)

# Prediction
def predict_price(model, area, bhk,bath,balcony, region_name, loc_mean):
    region_encoded_value = region_encode(region_name, loc_mean)
    
    if region_encoded_value is None:
        return f"Region '{region_name}' not found in the encoding mapping."
    
    input_data = [[area, bhk,bath,balcony, region_encoded_value]]
    
    predicted_price = model.predict(input_data)[0]
    
    return f"Predicted Price for {area} sqft, {bhk} BHK in region '{region_name}': {predicted_price:.2f}"
prediction = model.predict([[1200,1,1]])
print(prediction)
with open("bang_model.pkl","wb") as f:
    pickle.dump(model,f)






