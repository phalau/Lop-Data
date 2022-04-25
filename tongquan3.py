# Tìm hiểu xem dữ liệu được thống kê cho những ngày nào
from dataclasses import dataclass
import pandas as pd
import numpy as np
import json

df = pd.read_csv("/Volumes/DATA/Python/Lopdata/Data/subset-covid-data.csv")
df["date"].value_counts()
print(df["date"].value_counts())