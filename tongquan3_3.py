#Lấy ra 5 quốc gia có số ca nhiễm mới cao nhất
import pandas as pd
import numpy as np
import json

df = pd.read_csv("/Volumes/DATA/Python/Lopdata/Data/subset-covid-data.csv")
df = df.sort_values('cases',ascending = False)
df.head(5)
print ("5 quốc gia có số ca nhiễm mới cao nhất" + str(df.head(5)))