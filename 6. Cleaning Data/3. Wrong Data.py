#Pandas - Fixing Wrong Data
# import pandas as pd

# df = pd.read_csv('6. Cleaning Data/data.csv')
# print(df.to_string())

# df.loc[7,'Duration']=45 #Locate Row , 7 row ki duration change
# print(df.to_string())


#Loop through all values in the "Duration" coloumn.

#If the value is higher than 120, set it to 120:

import pandas as pd

df = pd.read_csv('6. Cleaning Data/data.csv')
print(df.to_string())

for x in df.index:
    # print(x)
    if df.loc[x,"Duration"]>120:
        df.loc[x,"Duration"]=129

print(df.to_string())        