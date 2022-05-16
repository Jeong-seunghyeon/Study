import pandas as pd
import numpy as np

Bodyheight = [1.62, 1.72, 1.55, 1.7, 1.78, 1.65, 1.64, 1.64, 1.66, 1.74]

ser = pd.Series(Bodyheight)
print(ser.describe())
