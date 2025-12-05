#used this to get the summarised csv file info

import pandas as pd

df = pd.read_csv("cancer_risk.csv")

# output the first 5 rows of the table
print(df.head())

# summarise the entire graph (this prints to console)
print(df.describe())

# summarise data columns
df.info()