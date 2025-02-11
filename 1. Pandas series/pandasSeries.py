#A pandas Series is like a column in a table.

#It is a one-dimensional array holding data of any type.

# import pandas as pd

# a=[1,2,7]

# myvar=pd.Series(a)

# print(myvar)
# #Labels
# # print(myvar[0])



# import pandas as pd

# a =[1, 7, 2]

# myvar=pd.Series(a,index=['x','y','z'])

# print(myvar)
# print(myvar["y"])


#Key/Value Object as Series
#create a simple pandas Series from a dictionary
#column
import pandas as pd

calories = {'day1': 420, 'day2':380, 'day3':390}

# myvar= pd.Series(calories)
myvar=pd.Series(calories,index=['day1','day2'])
print(myvar)