
# Số lượng dòng và cột của bộ dữ liệu
import pandas as pd
import numpy as np
import json

df = pd.read_csv("/Volumes/DATA/Python/Lopdata/Data/subset-covid-data.csv")
print(df.info())