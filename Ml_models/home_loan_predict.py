import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib
import plotly.express as px
import pickle

raw_df = pd.read_csv('homeloan.csv') 
raw_df['Gender'] = raw_df['Gender'].fillna(0) #replacing unknown with other 
df = raw_df[['Loan_ID','Gender','Married','Dependents','Education','ApplicantIncome','CoapplicantIncome','LoanAmount','Credit_History','Property_Area','Loan_Status']].dropna()
df = df[df['ApplicantIncome'] < 20000]
df['Gender'] = df['Gender'].replace(0, "Other")
#EDA
fig = px.scatter(df,x='ApplicantIncome',y='LoanAmount',color='Married')      
# fig.show()         
# Encoding 2 categorical coloumns
Mar_values = {'No': 0, 'Yes': 1}
df['Mar_numeric'] = df.Married.map(Mar_values)
Edu_value = {'Graduate' : 1, 'Not Graduate' : 1}
df['Edu_numeric']= df.Education.map(Edu_value)                                                                                  
train_df,test_df = train_test_split(df,train_size=0.1,random_state=21)
# model evaluation
model = LogisticRegression(solver='liblinear')
model.fit(train_df[['ApplicantIncome','CoapplicantIncome','LoanAmount','Mar_numeric','Edu_numeric']],train_df['Loan_Status'])
print(model.predict([[100,0,158,1,1]]))

with open("Loan_pred.pkl","wb") as f:
    pickle.dump(model,f)
    