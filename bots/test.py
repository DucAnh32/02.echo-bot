import pandas as pd
import numpy as np
df = pd.DataFrame({"STT": [1, 2, 3, 4, 5, 6,6, 7, 8], "val1": [1, 2, 3, 4, 5, 6,6, 7, 8], "val2": [1, 2, 3, 4, 5, np.nan,7, 7, 8]})
df=df.groupby('STT').agg({'val1':'sum','val2':'sum'})
print(df)
