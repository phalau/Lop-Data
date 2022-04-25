# lọc dữ liệu nhiễu:
import matplotlib as plt
import pandas as pd
import numpy as np
import json
df = pd.read_csv("/Volumes/DATA/Python/Lopdata/Data/subset-covid-data.csv")
df_locnhieu = df[df.date == '2020-04-12']
# Vẽ biểu đồ phân bố số lượng ca mắc mới ở các quốc gia
print ("trung bình số ca mắc mới: " + str(df_locnhieu .cases.mean()))
print ("trung vị của số ca mắc mới: "+ str(df_locnhieu .cases.median()))
import matplotlib.pyplot as plt
plt.hist(df_locnhieu.cases, bins = 200)
plt.title("Phân bố số ca mắc mới")
plt.xlabel("số số ca mắc mới")
plt.ylabel("Số lượng quốc gia")
plt.show()

