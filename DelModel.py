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
# making dataframes
raw_df = pd.read_csv('Delhi_v2.csv')
df = raw_df[['price','area','Bedrooms','Bathrooms','neworold']].dropna()
df = df[(df['price'] < 80000000)]
df = df[(df['area'] < 8000)]
train_df,test_df = train_test_split(df,test_size=0.1,random_state=42)

# model building
model = LinearRegression()
inputs = df[['area','Bedrooms','Bathrooms']]
targets = df['price']
model.fit(inputs,targets)
