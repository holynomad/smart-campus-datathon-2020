#label_capaNpcnt_iot_n_airinfo_200812.r (Team6)

library(dplyr)
library(readr)

# http://drtagkim.blogspot.com/2019/02/r-csv.html
# handle NA (missing values) https://akua0330.tistory.com/3
iot <- read_csv('iot_air_merged_20200625.csv')

head(iot)

# get another dataset about "outside air condition"
area <- read_csv('skf_area_tot.csv', col_names=c('roomid', 'roomnm', 'nm2', 'area', 'admin'))

head(area)
str(area)

# truncate third (building name) & fifth (administrator) column
# https://lightblog.tistory.com/7
area_rearr <- area[, -c(3,5)]

head(area_rearr)

# calculate "room capacity" & create new column
# https://ordo.tistory.com/10
area_rearr$capa <- floor(area_rearr$area / 3)

# let two of datasets merge each other ! using merge()
# https://lightblog.tistory.com/46
merge_one <- merge(iot, area_rearr, by="roomid")
head(merge_one, 30)

head(merge_one)

# random sampling "personCount" for new column
# https://m.blog.naver.com/PostView.nhn?blogId=jjy0501&logNo=220894428435&proxyReferer=https:%2F%2Fwww.google.com%2F
set.seed(1)
#area_rearr$personcnt <-sample(x=0:area_rearr$capa, size=1, replace = F)

# random "personCnt" from Normal dist.func.
# https://118k.tistory.com/862
# ref : https://data-make.tistory.com/63 [Data Makes Our Future]
for(i in 1:length(merge_one$capa)){
  merge_one$personcnt[i] <-sample(x=0:merge_one$capa[i], size=1)
}

head(merge_one$personcnt)
str(merge_one)

write.csv(merge_one, file="area_pcnt_rnorm_merged_20200625_v1.1.csv", row.names = FALSE)
