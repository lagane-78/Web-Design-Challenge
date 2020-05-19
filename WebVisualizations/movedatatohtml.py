import pandas as pd
import numpy as np

df = pd.read_csv("Resources/cities.csv")

df = df.rename(columns={"Unnamed: 0": "City_ID", })
print(df.head())

df.to_html('data.html',index=False)