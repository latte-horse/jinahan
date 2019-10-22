from rpy2.robjects import r

news_words = open('C:/Users/student/Documents/jinahan/통계분석/sample_file/words2.txt','r',encoding ='UTF-8')

print(news_words)

# news_data_count=news_words %>% select(V1)%>%
#   unnest_tokens_(input="V1",output="text")%>%count(text,sort = T)

# news_data_total=news_words %>% select(V1)%>%
#   unnest_tokens_(input="V1",output="text")%>%count(text,sort = T)%>%
#   summarize(total=sum(n))


# typeof(news_data_count)
# View(TF)
# View(news_data_count)
# print(news_data_count)

# TF=0
# for(i in 1:20){
#   news_data_count$n[i]
#   TF[i]=news_data_count$n[i]/news_data_total
#   print(TF)
# }  



