import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cancer_risk.csv")
plt.style.use('ggplot')

# create histograms
df.hist()

# create correlation graph with data distributions - df.plot.scatter(x=,y=)
# - replace x with the column you want to compare -
df.plot.scatter(x="Age", y = "Cancer_Risk_Score")

plt.show() # Display the histogram plots