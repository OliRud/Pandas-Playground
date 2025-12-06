#here is an attempt at producing an ai model using sci-kit learn

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

df = pd.read_csv("cancer_risk.csv")


#i begin by filling in missing values in the diet column with the diet mode
print(df["Diet_Category"].mode())
#using this, i can figure out that "Average" is the mode diet in this data.

#replacing missing values with the mode
df["Diet_Category"] = df["Diet_Category"].replace({np.nan: "Average"})

#fill entires for missing gene codes (this time using scikit)
imputer_for_genes = SimpleImputer(strategy="median")
result = imputer_for_genes.fit_transform(df[["Genetic_Marker_X"]])

df["Genetic_Marker_X"] = result.ravel() #rearange


from sklearn.preprocessing import OneHotEncoder

#converting diets into numeric refrence
ohe_diet = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
result = ohe_diet.fit_transform(df[["Diet_Category"]])

#develop the columns
col_names = ohe_diet.get_feature_names_out(["Diet_Category"])

df = df.drop(columns = ["Diet_Category"])
df = pd.concat([df, pd.DataFrame(result, columns = col_names)], axis = 1)


#replacing Smoker values from yes-no to 1-0 (using pandas)
df["Smoker"] = df["Smoker"].replace({"Yes" : 1, "No" : 0})


#removing columns which are not relevant or do not have correlation using graphs.py to find them
y = df["Cancer_Risk_Score"]
x = df.drop(columns=["Cancer_Risk_Score","Patient_ID","Zone","Hospital Number","Shoe_Size"])
#print(x.head())


#creating the test sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=43) #x,y, size of test data, seed


#normalising the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

if hasattr(x_train,"columns"): #scaling train
    x_train_scaled = pd.DataFrame(x_train_scaled, columns = x_train.columns, index = x_train.index)
if hasattr(x_test,"columns"): #scaling test
    x_test_scaled = pd.DataFrame(x_test_scaled, columns = x_test.columns, index = x_test.index)


#develop the linear model with the training data
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x_train_scaled, y_train)

y_pred = model.predict(x_train_scaled)

from sklearn.metrics import root_mean_squared_error

score = root_mean_squared_error(y_pred,y_train)

print(score)


# - When the model is ready, we can pop open the test - 