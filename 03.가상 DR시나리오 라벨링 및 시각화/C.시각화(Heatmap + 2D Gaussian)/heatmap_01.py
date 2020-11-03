#heatmap_01.py
#COVID 감염위험도 / 밀집도(Complexity) / 불쾌지수(DI) 시계열-room별 라벨링 시각화

import seaborn as sns
from matplotlib import pyplot as plt

# load dataset
import numpy as np
import pandas as pd

df = pd.read_csv("labelled_all_merged_0618_0702_v1.0.csv", encoding = 'euc-kr')

# https://hogni.tistory.com/7
#df_temp = df[["roomid", "datetime", "covid_case"]]
#df_temp = df[["roomid", "datetime", "di_case"]]
df_temp = df[["roomid", "datetime", "complx_case"]]

#print(df_temp.head())

df_temp_pv = df_temp.pivot('roomid', 'datetime', 'complx_case')

#print(df_temp_pv.head())

# exercise scatter plot
# #sns.regplot(x=df["roomid"], y=df["temp"])

# heatmap by plt.pcolor()
# 출처: https://rfriend.tistory.com/419 [R, Python 분석과 프로그래밍의 친구 (by R Friend)]
plt.pcolor(df_temp_pv)
plt.xticks(np.arange(0.5, len(df_temp_pv.columns), 1), df_temp_pv.columns)
plt.yticks(np.arange(0.5, len(df_temp_pv.index), 1), df_temp_pv.index)
plt.title('Comlexity risk map (0625~0702)', fontsize=20)
plt.xlabel('DateTime', fontsize=14)
plt.ylabel('RoomId', fontsize=14)
plt.colorbar()
plt.show()
