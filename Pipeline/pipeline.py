import sys
import pandas as pd

print("arguments", sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"Day": [1,2], "num_passenger": [3,4]})
df['month'] = month
print(df.head())

df.to_parquet(f"output_{month}.parquet")

print(f"Hello pipline, month = {month}")