#Lấy ra 5 quốc gia có số ca nhiễm mới cao nhất
import pandas as pd
import numpy as np
import json

df = pd.read_csv("/Volumes/DATA/Python/Lopdata/Data/subset-covid-data.csv")
soca_tv = df.sort_values('deaths',ascending = False)
soca_tv.head(5)
print ("5 quốc gia có số ca tử vong cao nhất" + str(soca_tv.head(5)))