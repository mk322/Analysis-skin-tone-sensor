import numpy as np

import pandas as pd

hand = pd.read_csv("rgb_hand.csv")
nail = pd.read_csv("rgb_nail.csv")
sensor = pd.read_csv("rgb_sensor1.csv")
#ssensor = pd.read_csv("srgb_sensor.csv")

result = pd.concat([hand, nail, sensor], axis=1)

#result['nail_distance'] = result.apply(lambda df: round(np.sqrt(np.square(df.red_nail-df.red_sensor)+np.square(df.green_nail-df.green_sensor)+np.square(df.blue_nail-df.blue_sensor)), 3), axis=1)
#result['hand_distance'] = result.apply(lambda df: round(np.sqrt(np.square(df.red_hand-df.red_sensor)+np.square(df.green_hand-df.green_sensor)+np.square(df.blue_hand-df.blue_sensor)), 3), axis=1)

result.to_csv("rgb_comparison_new.csv", index=False)