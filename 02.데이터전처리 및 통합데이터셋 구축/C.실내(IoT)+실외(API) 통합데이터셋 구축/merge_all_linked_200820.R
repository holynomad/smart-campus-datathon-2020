# merge_all_linked_200820.r (Team6)

library(dplyr)
library(readr)

# http://drtagkim.blogspot.com/2019/02/r-csv.html
# handle NA (missing values) https://akua0330.tistory.com/3
# read first csv
# ref. about 'korean encoding' -> http://drtagkim.blogspot.com/2019/02/r-csv.html
iot_01 <- read_csv('area_pcnt_rnorm_merged_20200618_v1.1.csv')
iot_02 <- read_csv('area_pcnt_rnorm_merged_20200625_v1.1.csv')
iot_03 <- read_csv('area_pcnt_rnorm_merged_20200702_v1.1.csv')

head(iot_01)
head(iot_02)
head(iot_03)

# convert POSIXlt to datetime format
iot_02$datetime <- as.POSIXlt(iot_02$datetime, format='%Y-%m-%d %H:%M:%S', tz=Sys.timezone())

# rbind all seperated_CSV files
iot_all <- rbind(iot_01, iot_02, iot_03)

# https://bpapa.tistory.com/20
# preprocessing col_names
colnames(iot_all) <- tolower(colnames(iot_all))
head(iot_all)

write.csv(iot_all, file="iot_allmerged_0618_0702.csv", fileEncoding = 'euc-kr', row.names = FALSE)
