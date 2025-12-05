#here is my attempt at producing an ai model using sci-kit 

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("cancer_risk.csv")


#i begin by filling in missing values in the diet column with the diet mode
print(df["Diet_Category"].mode())
#using this, i can figure out that "Average" is the mode diet in this data.

#replacing missing values with the mode
df["Diet_Category"] = df["Diet_Category"].replace({np.nan: "Average"})

#fill entires for missing gene codes
imputer_for_genes = SimpleImputer(strategy="median")
result = imputer_for_genes.fit_transform(df[["Genetic_Marker_X"]])

df["Genetic_Marker_X"] = result.ravel() #rearange

#replace missing values with the mode
df["Diet_Category"] = df["Diet_Category"].replace({np.nan: "Average"})
df.info()


