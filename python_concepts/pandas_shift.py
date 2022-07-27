import pandas as pd
import numpy as np

df = pd.DataFrame({"Col1": [10, 20, 15, 30, 45],
                   "Col2": [13, 23, 18, 33, 48],
                   "Col3": [17, 27, 22, 37, 52]},
                  index=pd.date_range("2020-01-01", "2020-01-05"))

df["Col2"] = df["Col2"].shift(periods=-1)
print(df)