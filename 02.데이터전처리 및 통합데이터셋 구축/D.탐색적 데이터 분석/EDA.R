#EDA.r (Team6)

library(dplyr)
library(readr)
library(ggplot2)

merged <- read_csv('iot_air_merged_20200618.csv')
merged_na <- merged %>% filter(!is.na(merged$roomid))

df_merged_na <- data.frame(time = merged_na$datetime, room = merged_na$roomid, fire = merged_na$fire, dust = merged_na$dust, temp = merged_na$temp, humid = merged_na$humid, co2 = merged_na$co2, move = merged_na$move, door = merged_na$door, so2 = merged_na$so2, o3 = merged_na$o3, pm2.5 = merged_na$pm2.5, pm10 = merged_na$pm10, no2 = merged_na$no2)

# https://jtoday.tistory.com/93
# EDA & visualization
#ggplot(data = df_merged_na) + geom_bar(mapping = aes(x=time))
#ggplot(data = df_merged_na) + geom_histogram(mapping = aes(x=time))

#dust
ggplot(data = df_merged_na, mapping = aes(x = dust, colour = )) + geom_freqpoly(binwidth = 0.1) + coord_cartesian(ylim = c(0, 10000), xlim = c(0, 250))

#humid
ggplot(data = df_merged_na, mapping = aes(x = humid, colour = )) + geom_freqpoly(binwidth = 0.1) + coord_cartesian(ylim = c(0, 25000))

#co2
ggplot(data = df_merged_na, mapping = aes(x = co2, colour = )) + geom_freqpoly(binwidth = 0.1) + coord_cartesian(ylim = c(0, 10000), xlim = c(500, 1500))
