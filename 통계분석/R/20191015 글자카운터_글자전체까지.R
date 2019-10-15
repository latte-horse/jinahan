library(dplyr)
library(tidytext)
library(janeaustenr)
install.packages('KoNLP')
library(KoNLP)
install.packages('rJava')
library(rJava)
install.packages('data.table')
library(data.table)
install.packages('ggplot2')
library(ggplot2)
rm(list=ls())
head(text)

news_words<-fread(file ='C:/Users/student/Desktop/PJ/통계분석/words.txt',encoding ='UTF-8')
  news_words %>% tail(1)
  print(news_words)

news_data_count=news_words %>% select(서울교통공사)%>%
  unnest_tokens_(input="서울교통공사",output="text")%>%count(text,sort = T)

news_data_total=news_words %>% select(서울교통공사)%>%
  unnest_tokens_(input="서울교통공사",output="text")%>%count(text,sort = T)%>%
  summarize(total=sum(n))


for(i in 1:20){
  TF[i]=news_data_count$n[i]/news_data_total
  print(TF)
}  
#nrow(news_data_count)
head(TF)


typeof(news_data_count)
View(TF)
View(news_data_count)
print(news_data_count)




