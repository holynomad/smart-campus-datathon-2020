# merge_iot_n_airinfo_200805.r (Team6)

library(dplyr)
library(readr)

# http://drtagkim.blogspot.com/2019/02/r-csv.html
# handle NA (missing values) https://akua0330.tistory.com/3
iot <- read_csv('iot_output_07020900.csv')

head(iot)

# truncate first (datetime_ms) & second (builiding ID) column
# https://lightblog.tistory.com/7
iot_rearr <- iot[, (3:11)]

head(iot_rearr)

# https://m.blog.naver.com/PostView.nhn?blogId=lool2389&logNo=220815116956&proxyReferer=https:%2F%2Fwww.google.com%2F
iot_rearr_trim <- iot_rearr

# https://datascienceschool.net/view-notebook/ee124776eea041059d2b1d4a0e0ecc2e/
# https://homy.tistory.com/3
iot_rearr_trim$datetime_hour <- format(iot_rearr$datetime_s, format="%Y-%m-%d %H")
iot_rearr_trim$datetime_minsec <- format(iot_rearr$datetime_s, format="%M:%S")

iot_rearr_trim$datetime <- format(iot_rearr$datetime_s, format="%Y-%m-%d %H:%M:%S")

head(iot_rearr_trim, 5)

# get another dataset about "outside air condition"
aircond <- read_csv('air_output_sample_10000row.csv')

head(aircond)

# trimming first column format (datetime_s)
aircond_trim <- aircond
aircond_trim$datetime_hour <- format(aircond$datatime, format="%Y-%m-%d %H")
aircond_trim$datetime_minsec <- format(aircond$datatime, format="%M:%S")


head(aircond_trim, 5)

# https://realab.tistory.com/8
#names(iot_rearr_trim)
#names(iot_rearr_trim)[1] <- c("datatime")
#names(iot_rearr_trim)

# let two of datasets merge each other ! using merge()
# https://lightblog.tistory.com/46
merge_one <- merge(iot_rearr_trim, aircond_trim, by="datetime_hour")
head(merge_one, 30)

# get merge_one "data.framed format" !!
# https://ybeaning.tistory.com/8
attach(merge_one)
df_merge_one <- data.frame(datetime, roomid, fire, dust, temp, humid, co2, move, door, so2, o3, no2, pm10, pm10_24, pm10_grade, pm10_grade_1h, pm2.5, pm2.5_24, pm2.5_grade, pm2.5_grade_1h, khai, khai_grade, so2_grade, co_grade, o3_grade, no2_grade, stringsAsFactors = F)
detach(merge_one)

# remove NA rows (roomid is NA) using "filter"
# https://kucoma112.tistory.com/17
df_merge_one_na <- df_merge_one %>% filter(!is.na(roomid))

head(df_merge_one_na)
str(df_merge_one)

write.csv(df_merge_one_na, file="iot_air_merged_20200702.csv", row.names = FALSE)
