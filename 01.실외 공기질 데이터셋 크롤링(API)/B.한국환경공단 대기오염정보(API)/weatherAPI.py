# 기상청 <동네예보 조회서비스> API 가져오기 (참조 : http://makeshare.org/bbs/board.php?bo_table=raspberrypi&wr_id=63 수정필요)

import urllib.request
import json
import datetime
import pytz
import requests
import pandas as pd

def get_weather_data() :
    api_date = "20200611"
    api_time = "0830"

    endpoint = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst" # 참조 : https://signing.tistory.com/22
    key = "?serviceKey=ReplaceYourKey"
    pageNo = "&pageNo=1"
    date = "&base_date=" + api_date
    time = "&base_time=" + api_time
    dataType = "&dataType=JSON"
    nx = "&nx=61"
    ny = "&ny=127"  # 서울시 성북구 안암동
    numOfRows = "&numOfRows=100"
    api_url = endpoint + key + pageNo + numOfRows + dataType + date + time + nx + ny

    data = urllib.request.urlopen(api_url).read().decode('utf8')
    data_json = json.loads(data)
    parsed_json = data_json['response']['body']['items']['item']

    target_date = parsed_json[0]['baseDate']
    target_time = parsed_json[0]['baseTime']
    date_calibrate = target_date

    if target_time > '1300':
        date_calibrate = str(int(target_date) + 1)

    passing_data = {}
    for one_parsed in parsed_json:
        if one_parsed['baseDate'] == target_date and one_parsed['baseTime'] == target_time: #get today's data
            passing_data[one_parsed['category']] = one_parsed['obsrValue']

        if one_parsed['baseDate'] == date_calibrate and (
                one_parsed['category'] == 'TMX' or one_parsed['category'] == 'TMN'): #TMX, TMN at calibrated day
            passing_data[one_parsed['category']] = one_parsed['obsrValue']

    return passing_data

# 현 시점 date + time 읽어오기
def get_api_date() :
    standard_time = [2, 5, 8, 11, 14, 17, 20, 23] #api response time
    time_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%H') #get hour
    check_time = int(time_now) - 1
    day_calibrate = 0

	#hour to api time
    while not check_time in standard_time :
        check_time -= 1
        if check_time < 2 :
            day_calibrate = 1 # yesterday
            check_time = 23

    date_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%Y%m%d') #get date
    check_date = int(date_now) - day_calibrate

    if len(str(check_time)) < 2:
        correct_time = '0' + str(check_time)
    else:
        correct_time = str(check_time)

    return (str(check_date), (correct_time + '00')) #return date(yyyymmdd), tt00

# 출처: https://ssoonidev.tistory.com/102 [심심해서 하는 블로그]
def call_weather_api(start_date, end_date):
    #api_key = open("./raw_data/weather_api").readlines()[0].strip()
    #url_format = 'https://data.kma.go.kr/apiData/getData?type=json&dataCd=ASOS&dateCd=HR&startDt={date}&startHh=00&endDt={date}&endHh=23&stnIds={snt_id}&schListCnt=100&pageIndex=1&apiKey={api_key}'


    headers = {'content-type': 'application/json;charset=utf-8'}
    for date in pd.date_range(start_date, end_date).strftime("%Y%m%d"):
        print("%s Weather" % date)

        time = '0900'

        endpoint = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst" # 참조 : https://signing.tistory.com/22
        key = "?serviceKey=ReplaceYourKey"
        pageNo = "&pageNo=1"
        basedate = "&base_date=" + date
        basetime = "&base_time=" + time
        dataType = "&dataType=JSON"
        nx = "&nx=61"
        ny = "&ny=127"  # 서울시 성북구 안암동
        numOfRows = "&numOfRows=100"
        api_url = endpoint + key + pageNo + numOfRows + dataType + basedate + basetime + nx + ny

        response = requests.get(api_url, headers=headers, verify=False)

        print(response.json()['response']['body']['items'])

        result = pd.DataFrame(response.json()['response']['body']['items']['item'], columns=['baseDate', 'baseTime', 'category', 'nx', 'ny', 'obsrValue'])

        print(result.head())

        result.to_csv("./weatherInfo_%s.csv" % date, index=False, encoding="utf-8")

# 메인 static method
if __name__ == '__main__':
    print(get_weather_data())
    call_weather_api('20200730', '20200730')
