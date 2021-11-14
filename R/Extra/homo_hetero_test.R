#test for homoscedasticity and heteroscedasticity
#dataset: cars (inbuilt)

library(MASS) #box-cox transform
#install.packages("lmtest")
library(lmtest) #bp test
library(car) #ncv test

cars=cars
head(cars)
#View(cars)

#to predict the distance Y
#buiding the linear regression model
colnames(cars)
nrow(cars)

tot=nrow(cars)
s=sample(seq(1:tot),0.7*tot)
train=cars[s,]
test=cars[-s,]


m1=lm(dist~speed,data=train )

#plot error component vs the y variable
err=m1$residuals
y=train$dist

plot(y,err,main="model 1")
abline(0,0, col="blue")

#test for heteroscedasticity

# 1. Breusch_pagan Test
bptest(m1)

# ncv test
ncvTest(m1)

#box-cox transformation of y-var
dist_bc=boxcox(dist~speed,data=train)

dist_bc

#find optimual lambda value
lambda=dist_bc$x[which(dist_bc$y==max(dist_bc$y))]

#convert y variable into a boxcox trsfowmation using the lambda value
d1=y^lambda
cbind(y,d1)

#add this new dq in the train and test data
train$dist1=d1
head(train)




#model 2 (new Y)~X ie the box cox model
m2=lm(dist1~speed,data=train)

bptest(m2)

#plot the residulas and the Y-variable
plot(train$dist1,m2$residuals)
abline(0,0,col="blue")




#model 3, use Y -> Dist (original)
#use log(speed) as X
log_speed=log(train$speed,2)
train$speed1=log_speed

m3=lm(dist~log_speed,data=train)

#plot the residulas and the Y-variable
plot(train$dist,m3$residuals)
abline(0,0,col="blue")

bptest(m3)
ncvTest(m3)
