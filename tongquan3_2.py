#Tổng số ca mắc mới, số ca tử vong ở từng châu lục
import pandas as pd
import numpy as np
import json
df = pd.read_csv("/Volumes/DATA/Python/Lopdata/Data/subset-covid-data.csv")
df_locnhieu = df[df.date == '2020-04-12']
# print("tổng số ca nhiễm và số ca tử vong của các châu lục")
tong_ca_nhiem = df_locnhieu.groupby('continent')['cases','deaths'].sum()
print("tổng số ca nhiễm và số ca tử vong của các châu lục" +str(tong_ca_nhiem))