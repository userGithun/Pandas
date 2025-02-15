import pandas as pd

df=pd.read_csv('3. read CSV/data.csv')

print(df.to_string())
print(df)

print(pd.options.display.max_rows)


# Increase the maximun number of rows to display the entire DataFrames:
import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('3. Read CSV/data.csv')

print(df)