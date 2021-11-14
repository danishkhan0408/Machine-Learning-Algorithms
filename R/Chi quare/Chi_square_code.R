#Chi square test
col1=c(560,495,553,547,512,369,385,358,361,393,209,226,248,268,285,267,277,304,328,340,64,70,93,77,126)
mx1= matrix(col1,ncol=5,byrow=T)
View(mx1)
chi_sq=chisq.test(mx1)
print(chi_sq)  
#p value is very high and lesser than 0.05 -> reject the Null Hypo 
#Accept the Alternate hypo