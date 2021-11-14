#Anova test
#data set of training programs effectiveness on productivity
p1=c(NA,15,18,19,22,11)
p2=c(NA,22,27,18,21,17)
p3=c(18,24,19,16,22,15)
df=data.frame(p1,p2,p3)

#stack the data 
stack_df=stack(df)
View(stack_df)
print(stack_df)

#anova function
av_prod=aov(values~ind,data=stack_df)
summary(av_prod)
