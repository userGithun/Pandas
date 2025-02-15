# #Return a new Data Frame with no empty cells:
# #original file par kabhi work nahi karo

# import pandas as pd

# df = pd.read_csv('6. Cleaning Data/data.csv')

# print(df.to_string())

# new_df =df.dropna()
# print(new_df.to_string()) #Complete set data

#Note: By default, the dropna() method retunrs a new DataFrame, and will not change the original.


#If you want to change the original DataFrame, use the inplace = True argument:
#Remove all rows with NULL(NaN) values:
# import pandas as pd

# df = pd.read_csv('6. Cleaning Data/data.csv')
# print(df.to_string())

# df.dropna(inplace= True)

# print(df.to_string())




# Replace Empty Values
# import pandas as pd

# df = pd.read_csv('6. Cleaning Data/data.csv')
# print(df.to_string())

# df.fillna(130,inplace= True)

# print(df.to_string())


# #Replace Only for Specified coloums
# import pandas as pd

# df = pd.read_csv('6. Cleaning Data/data.csv')
# print(df.to_string())

# df['Calories'].fillna(130,inplace= True)

# print(df.to_string())


import pandas as pd

df = pd.read_csv('6. Cleaning Data/data.csv')
# print(df.to_string())

x = df["Calories"].mean()  #average valuie nikalega
x = df["Calories"].median()  #jo value median mai hoti hai ushe replacing kar deta hai accending or decending ke hisab se dekhta hai
x = df["Calories"].mode()[0]  #jo value bahut jada user hoti hai ush value ko baha par rakh deta hai

# df["Calories"].fillna(x,inplace= True)
print(df.to_string())


