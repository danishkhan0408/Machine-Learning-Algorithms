library(stringi)
#generate customer id
custid=seq(21,40)
#generate customer name of length 5
name=stri_rand_strings(20,5,'[a-zA-Z]')
#generate mobile numbers
phone=runif(20,9000000000,9999999999)
age=sample(c(18:50),20)
gen=c("M","F")
gender=sample(gen,20,replace = T)
print(gender)
sample(gender)
balance=round(runif(20,100000,10000000),2)
domain=c('@gmail.com','@hotmail.com','@yahoo.co.in','@outlook.com')
email=c()
for(i in name)
{
  j=sample(seq(1:length(domain)),1)
  em=paste(i,domain[j],sep="")
  email=c(email,em)
}
bank1=data.frame(custid,name,age,gender,phone,balance,email)
bank=data.frame(custid,name,age,gender,phone,balance,email)
View(bank)
str(bank)

#fix data type
bank$name=as.character(bank$name)
bank$email=as.character(bank$email)
str(bank)

cscore=sample(c(300:900),20)
print(cscore)
priv=rep(c('Y','N'),times=c(5,15))
bank1$credt_score=cscore
bank1$privilege=priv
View(bank)
bank1$priv=sample(bank$priv)
View((bank))
bank1$privilege[(bank1$credt_score>=600)]='Y'
bank1$privilege[(bank1$credt_score<600)]='N'
View(bank)

#new data frame
View(bank1)
str(bank1)
bank1$name=as.character((bank1$name))
bank1$email=as.character(bank1$email)
View(bank1)
str(bank1)
bank1$priv=NULL

#combine the two data frames
bank=rbind(bank,bank1)
View(bank)