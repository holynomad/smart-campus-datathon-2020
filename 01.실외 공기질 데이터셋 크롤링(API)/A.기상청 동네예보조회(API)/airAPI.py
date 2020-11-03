# airAPI.py (참조 : https://www.lightsky.kr/140)

import requests
from bs4 import BeautifulSoup
import pandas as pd

api_key = 'InsertYourKey'
params = '&numOfRows=10000&pageNo=1&stationName=동대문구&dataTerm=3MONTH&ver=1.3'
api_url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=' + api_key + params

# 참조 : https://javan.tistory.com/1
df = pd.DataFrame(columns=['datatime', 'mangname', 'so2', 'o3', 'no2', 'pm10', 'pm10_24', 'pm2.5', 'pm2.5_24', 'khai', 'khai_grade', 'so2_grade', 'co_grade', 'o3_grade', 'no2_grade', 'pm10_grade', 'pm2.5_grade', 'pm10_grade_1h', 'pm2.5_grade_1h'])

i=0

res = requests.get(api_url)
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.find_all('item')

for item in data:

    time = item.find('datatime')
    name = item.find('mangname')
    so2 = item.find('so2value')
    o3  = item.find('o3value')
    no2 = item.find('no2value')
    pm10 = item.find('pm10value')
    pm1024 = item.find('pm10value24')
    pm25 = item.find('pm25value')
    pm2524 = item.find('pm25value24')
    khai = item.find('khaivalue')
    khaigr = item.find('khaigrade')
    so2gr = item.find('so2grade')
    cogr = item.find('cograde')
    o3gr = item.find('o3grade')
    no2gr = item.find('no2grade')
    pm10gr = item.find('pm10grade')
    pm25gr = item.find('pm25grade')
    pm10gr1h = item.find('pm10grade1h')
    pm25gr1h = item.find('pm25grade1h')

    df.loc[i] = [time.get_text(), name.get_text(), so2.get_text(), o3.get_text(), no2.get_text(), pm10.get_text(), pm1024.get_text(), pm25.get_text(), pm2524.get_text(),
    khai.get_text(), khaigr.get_text(), so2gr.get_text(), cogr.get_text(), o3gr.get_text(), no2gr.get_text(), pm10gr.get_text(), pm25gr.get_text(), pm10gr1h.get_text(), pm25gr1h.get_text()]
    i=i+1

df.to_csv('air_output_sample_10000row.csv', encoding='euc-kr', index=False)
