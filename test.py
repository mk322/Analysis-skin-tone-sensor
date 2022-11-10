import pandas as pd

df = pd.read_csv("unidentifiable_data.csv")

df['red_sensor'] = df.apply(lambda row: (row.R >> 8), axis=1)
df['green_sensor'] = df.apply(lambda row: (row.G >> 8), axis=1)
df['blue_sensor'] = df.apply(lambda row: (row.B >> 8), axis=1)

output = df[['red_sensor', "green_sensor", "blue_sensor"]].copy()
output.to_csv("rgb_sensor1.csv", index=False)