#A Pandas DataFrame is a 2 dimensional data structure,like a 2 dimensional array, or a table with rows and columns.

import pandas as pd

data={
    #dictionary
    "calories":[420, 380, 390],
    "duration":[50, 40 ,45]
}

#load data into a DataFrames object:
df= pd.DataFrame(data)
print(df)
# print(df.loc[0])#Locate Row series ke form mai
#use a list of indexes:
print(df.loc[[0,1]]) #DataFrame