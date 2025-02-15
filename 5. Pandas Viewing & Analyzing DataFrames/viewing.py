import pandas as pd

df = pd.read_csv('5. Pandas Viewing & Analyzing DataFrames/data.csv')

# print(df)
# print(df.to_string())
# print(df.head(10)) #suru ke 10 print krega
# print(df.head()) #start 5 row , normaly suru ke 5 print krega
# print(df.tail()) #last row 5 dataframe , normaly last ke 5 print krega
print(df.info()) #information about the data set