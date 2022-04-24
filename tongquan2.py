
import pandas as pd
import numpy as np
import json

df = pd.read_csv("/Volumes/DATA/Python/Lopdata/Data/subset-covid-data.csv")
df['new_col'] = np.nan
df['new_col1'] = 19
del df['new_col1']

df.info
# Số lượng dòng và cột của bộ dữ liệu
import pandas as pd
import numpy as np
import json

df = pd.read_csv("/Volumes/DATA/Python/Lopdata/Data/subset-covid-data.csv")

print(df.info)