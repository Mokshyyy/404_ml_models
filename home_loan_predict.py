import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler
raw_df = pd.read_csv('homeloan.csv') 
raw_df['Gender'] = raw_df['Gender'].fillna(0) 
df = raw_df[['Loan_ID','Gender','Married','Education','ApplicantIncome','CoapplicantIncome','LoanAmount','Credit_History','Property_Area','Loan_Status']].dropna()
df = df[df['ApplicantIncome'] < 20000]
df['Gender'] = df['Gender'].replace(0, "Other")
#EDA
fig = px.scatter(df,x='ApplicantIncome',y='LoanAmount',color='Married')      
# fig.show()         
# Encoding 2 categorical coloumns
Mar_values = {'No': 0, 'Yes': 1}
Mar_numeric = df.Married.map(Mar_values)
Edu_value = {'Graduate' : 1, 'Not Graduate' : 1}
Edu_numeric = df.Education.map(Edu_value)                                                                                  
train_df,test_df = train_test_split(df,train_size=0.1,random_state=21)
# scalling numeric data like income and loan amount
scaler = MinMaxScaler()
scaler.fit(train_df[['ApplicantIncome','CoapplicantIncome','LoanAmount']])
train_df[['ApplicantIncome','CoapplicantIncome','LoanAmount']] = scaler.transform(train_df[['ApplicantIncome','CoapplicantIncome','LoanAmount']]) # scales data from (0,1) range proportionally

