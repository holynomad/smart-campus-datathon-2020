#-*- coding: utf-8 -*-  #한글을 쓸 때는 꼭 붙인다. 문자 인코딩을 UTF-8로 하겠다는 것이다.
# KU데이터톤에서 주어진 IoT 데이터셋(txt)을 가공하기 위해 CSV로 일괄변환
# txt2csv.py

import csv
import pandas as pd
import os


# 참조 : https://m.blog.naver.com/PostView.nhn?blogId=resumet&logNo=221449693886&proxyReferer=https:%2F%2Fwww.google.com%2F
df = pd.read_table('iot_11_5325.txt', sep='|') #, names=['datetime_ms', 'buildingid', 'datetime_s', 'fire', 'dust', 'temp', 'humid', 'co2', 'move', 'door', 'roomid'])

df2 = pd.DataFrame(df)
print(df2.shape)

### columns=['datetime_ms', 'buildingid', 'datetime_s', 'fire', 'dust', 'temp', 'humid', 'co2', 'move', 'door', 'roomid'],

df2.to_csv('iot_output_07020900.csv', sep=',', index=False)
print(df2.tail(5))
