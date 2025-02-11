import pandas as pd

df = pd.read_json('4. Read JSON/data.json')

print(df.to_string())