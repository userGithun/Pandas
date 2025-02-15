#Cleaning Data of Wrong Format
import pandas as pd

df =pd.read_csv('6. Cleaning Data/data.csv')
# print(df.to_string())
df['Date']=pd.to_datetime(df['Date'])
df.dropna(subset=['Data'],inplace= True)

print(df.to_string())