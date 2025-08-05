import pandas as pd 
from constants import DATA_PATH

df = pd.read_csv(DATA_PATH / "titanic.csv")

print(df.head())