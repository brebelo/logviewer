import pandas as pd

df = pd.read_csv('InfoLog54.csv', skiprows=5002)

print(df.head())