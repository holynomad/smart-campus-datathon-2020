#label_all_Y_merged_200826.r (Team6)

library(dplyr)
library(readr)

# http://drtagkim.blogspot.com/2019/02/r-csv.html
# handle NA (missing values) https://akua0330.tistory.com/3
merged_one <- read_csv('iot_allmerged_0618_0702.csv', locale=locale('ko', encoding='euc-kr'))

head(merged_one)

# DR (Disaster Recovery) case labelling
for(i in 1:length(merged_one$capa)){
  merged_one$di_case[i] <- ifelse(merged_one$temp[i]-0.55*(1-0.01*merged_one$humid[i])*(merged_one$temp[i]-14.5) >= 24.4, 5,
                                  ifelse(merged_one$temp[i]-0.55*(1-0.01*merged_one$humid[i])*(merged_one$temp[i]-14.5) >= 24.1, 4,
                                         ifelse(merged_one$temp[i]-0.55*(1-0.01*merged_one$humid[i])*(merged_one$temp[i]-14.5) >= 23.9, 3,
                                                ifelse(merged_one$temp[i]-0.55*(1-0.01*merged_one$humid[i])*(merged_one$temp[i]-14.5) >= 23.8, 2,
                                                       ifelse(merged_one$temp[i]-0.55*(1-0.01*merged_one$humid[i])*(merged_one$temp[i]-14.5) >= 23.7, 1, 0)))))

  merged_one$clean_case[i] <- ifelse(merged_one$dust[i] <= 14, 5,
                                     ifelse(merged_one$dust[i] <= 17, 4,
                                            ifelse(merged_one$dust[i] <= 19, 3,
                                                   ifelse(merged_one$dust[i] <= 20, 2,
                                                          ifelse(merged_one$dust[i] <= 22, 1, 0)))))

  merged_one$fire_case[i] <- ifelse(merged_one$fire[i] == 1 & merged_one$temp[i] >= 27.9, 5,
                                    ifelse(merged_one$fire[i] == 1 & merged_one$temp[i] >= 27.5, 4,
                                           ifelse(merged_one$fire[i] == 1 & merged_one$temp[i] >= 27.3, 3,
                                                  ifelse(merged_one$fire[i] == 1 & merged_one$temp[i] >= 27.1, 2,
                                                         ifelse(merged_one$fire[i] == 1 & merged_one$temp[i] >= 26.9, 1, 0)))))

  merged_one$complx_case[i] <- ifelse(merged_one$co2[i] >= 1953 & merged_one$personcnt[i]/merged_one$capa[i] >= 0.7, 5,
                                      ifelse(merged_one$co2[i] >= 1838 & merged_one$personcnt[i]/merged_one$capa[i] >= 0.7, 4,
                                             ifelse(merged_one$co2[i] >= 1766 & merged_one$personcnt[i]/merged_one$capa[i] >= 0.7, 3,
                                                    ifelse(merged_one$co2[i] >= 1712 & merged_one$personcnt[i]/merged_one$capa[i] >= 0.7, 2,
                                                           ifelse(merged_one$co2[i] >= 1669 & merged_one$personcnt[i]/merged_one$capa[i] >= 0.7, 1, 0)))))

  merged_one$covid_case[i] <- ifelse(merged_one$complx_case[i] == 5 & merged_one$humid[i] <= 40, 5,
                                     ifelse(merged_one$complx_case[i] == 4 & merged_one$humid[i] <= 45, 4,
                                            ifelse(merged_one$complx_case[i] == 3 & merged_one$humid[i] <= 50, 3,
                                                   ifelse(merged_one$complx_case[i] == 2 & merged_one$humid[i] <= 55, 2,
                                                          ifelse(merged_one$complx_case[i] == 1 & merged_one$humid[i] <= 60, 1, 0)))))

  # reference logic (below)
  #merged_one$covid_case[i] <- ifelse(merged_one$complx_case[i] >= 2 & merged_one$humid[i] <= 58, 1, 0)

  # exception handling about covid_case : & merged_one$pm2.5[i] > 36 & merged_one$pm10[i] > 81
  #merged_one$personcnt[i] <-abs(round(rnorm(n=merged_one$capa[i], mean=0, sd=1)))
  #merged_one$di_case[i] <- ifelse(merged_one$temp[i]-0.55*(1-0.01*merged_one$humid[i])*(merged_one$temp[i]-14.5) >= 23.7, 1, 0)
  #merged_one$clean_case[i] <- ifelse(merged_one$dust[i] <= 22.1, 1, 0)
  #merged_one$fire_case[i] <- ifelse(merged_one$fire[i] == 1 & merged_one$temp[i] >= 26.9, 1, 0)
  #merged_one$complx_case[i] <- ifelse(merged_one$co2[i] >= 900 & merged_one$personcnt[i]/merged_one$capa[i] >= 0.7, 1, 0)

}

#str(merged_one)

write.csv(merged_one, file="labelled_all_merged_0618_0702_v1.0.csv", fileEncoding = 'euc-kr', row.names = FALSE)
