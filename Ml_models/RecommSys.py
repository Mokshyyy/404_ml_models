#importing lib
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import coo_matrix
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
#making df
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
#splitting df
train_df,test_df = train_test_split(rec_df,test_size=0.5,random_state=42)
# print(rec_df.tags)
input_tag = ["Apartment, Semi-Furnished, 2 BHK, 2 Bathrooms, 1 Balcony, Gym, Park"]
Tfidf_Vectorizer = TfidfVectorizer()
vector_matrix = Tfidf_Vectorizer.fit_transform(train_df['tags'])
input_vector = Tfidf_Vectorizer.transform(input_tag) 
rec_sys = cosine_similarity(input_vector,vector_matrix)
top_indices = rec_sys.argsort()[0][-5:][::-1]    
print(rec_df.city.unique())
#print("Top 5 Similar Listings:")
#for idx in top_indices:
 #   print(rec_df.iloc[idx]['tags'])
