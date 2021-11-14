# this is the working version.. for use in demo.. (WITH CHANGES.. CRS)
# Objective of knn() : to classify dataset into categories based on 
# different variables
# dataset: GLASS
# type: Classification
# attributes: Integer/Long

# include libraries
library(class)
library(caret)

# select the input dataset
# glass = file.choose()
path="C:/Users/Danish/Desktop/Data science/knn/glass.csv"
glass = read.csv(path,header=T)
View(glass)
head(glass)
# remove this variable as it is not required for SVM
glass$id_number=NULL

# Numeric Check
# 1) Do all the numeric checks
# 2) Check for multicollinearity

# KNN requires that the data be scaled/standardized for more accurate prediction. 
# to do this, do a Summary of the dataset and decide if it requires scaling or not
# include only the predictor variables (X1,... Xn), don't standardize the y-variable
# summary(glass[,c(2:10)])
summary(glass)

# for a good model building process, 
# 1) build model without standardization
# 2) build model with standardization
# 3) compare 1 and 2

# minmax function to be applied to the input dataset
minmax = function(x) return( (x-min(x))/(max(x)-min(x)) )

# scale the dataset
# get the column number of the target(Y) variable from the original dataset
# method 1
target_col_number = grep("Type", colnames(glass))
print(target_col_number)

# method 2
target_col_number = which(colnames(glass)=="Type"); print(target_col_number)

glass_scale = as.data.frame(lapply(glass[,-target_col_number], minmax))
View(glass_scale)
head(glass_scale)
summary(glass_scale)
### KNN scaling ends here ###
# adding the y variable from the original data set and placing it into the new scaled dataset
glass_scale[target_col_number] = glass[target_col_number]
head(glass_scale)
levels(factor(glass_scale$Type))

# since dataset is grouped based on Type, randomly shuffle it 
# runif() - random number based on uniform distribution
grp = runif(nrow(glass_scale))
glass_scale = glass_scale[order(grp),]

# split data into training and test
sample_size = floor(0.7*nrow(glass_scale))
sample_ind = sample(seq_len(nrow(glass_scale)), sample_size)
train = glass_scale[sample_ind,]
test=glass_scale[-sample_ind,]
nrow(train); nrow(test)

# check if the classes are present in both train and test
levels(factor(train$Type))
levels(factor(test$Type))

# set the target variable(Y) for training and testing
traintarget=train$Type
testtarget=test$Type
length(traintarget); length(testtarget)

# remove the Y-variable from the train and test dataset
train$Type=NULL; test$Type=NULL

# do a cross-validation to determine the value of K
# pick K which has the maximum accuracy of predictions
# model_knncv = knn.cv(trainingdata, traintarget, k=1)
# cv_accuracy = length(which(model_knncv==traintarget, T)) / length(model_knncv)
# for k=1..n

result = c(NA)
#default code, not an efficient method since k=1 is highly biased
#and k=even is not preferred
cv_accuracy = c()
for (i in seq(1,20))
{
    # check the CV with train_x variables with the train_Y_variables
    model_knncv = knn.cv(train, traintarget, k=i)
    cv_accuracy[i] = length(which(model_knncv==traintarget, T)) / length(model_knncv)
}

for(i in 1:20)
print(paste("Neighbours=",i, ". Accuracy=",round(cv_accuracy[i],2)))

#optimized code since K = odd number and ideally between 3 and 11 for classification
cv_accuracy1 = c()
count=1
for(i in seq(3,11,2))
{
  # check the CV with train_x variables with the train_Y_variables
  model_knncv1 = knn.cv(train, traintarget, k=i)
  cv_accuracy1[count] = length(which(model_knncv1==traintarget, T)) / length(model_knncv1)
  count= count+1
}
cv_accuracy1
count=1
for(i in seq(3,11,2))
 {
  print(paste("Neighbours=",i, ". Accuracy=",round(cv_accuracy1[count],4)))
  count = count + 1
}
max(cv_accuracy1)
# take the prediction that gives the maximum accuracy
#neighbours = which(cv_accuracy == max(cv_accuracy))
#print(paste("optimum neighbours=",neighbours))

# take the prediction that gives the maximum accuracy
neighbours = which(cv_accuracy1 == max(cv_accuracy1)) +2
#neighbours = 5 #taking max is 5
print(paste("optimum neighbours=",neighbours))

# knn() takes 4 params - Training dataset, Test dataset, Factor(training target), k=<n>
predict_target = knn(train, test, traintarget, k=neighbours)

# create confusion matrix to determine the accuracy
confusionMatrix(as.factor(testtarget), as.factor(predict_target))










# build the next model with the Actual dataset

target_col_number = grep("Type", colnames(glass))
print(target_col_number)

# method 2
target_col_number = which(colnames(glass)=="Type"); print(target_col_number)
glass_scale1=as.data.frame(glass[,-target_col_number])
#glass_scale = as.data.frame(lapply(glass[,-target_col_number], minmax))
View(glass_scale1)
head(glass_scale1)
summary(glass_scale1)
### KNN scaling ends here ###
# adding the y variable from the original data set and placing it into the new scaled dataset
glass_scale1[target_col_number] = glass[target_col_number]
head(glass_scale1)
levels(factor(glass_scale1$Type))

# since dataset is grouped based on Type, randomly shuffle it 
# runif() - random number based on uniform distribution
grp = runif(nrow(glass_scale1))
glass_scale1 = glass_scale1[order(grp),]

# split data into training and test
sample_size = floor(0.7*nrow(glass_scale1))
sample_ind = sample(seq_len(nrow(glass_scale1)), sample_size)
train = glass_scale1[sample_ind,]
test=glass_scale1[-sample_ind,]
nrow(train); nrow(test)

# check if the classes are present in both train and test
levels(factor(train$Type))
levels(factor(test$Type))

# set the target variable(Y) for training and testing
traintarget=train$Type
testtarget=test$Type
length(traintarget); length(testtarget)

# remove the Y-variable from the train and test dataset
train$Type=NULL; test$Type=NULL

# do a cross-validation to determine the value of K
# pick K which has the maximum accuracy of predictions
# model_knncv = knn.cv(trainingdata, traintarget, k=1)
# cv_accuracy = length(which(model_knncv==traintarget, T)) / length(model_knncv)
# for k=1..n

result = c(NA)
#optimized code since K = odd number and ideally between 3 and 11 for classification
cv_accuracy2 = c()
count=1
for(i in seq(3,11,2))
{
  # check the CV with train_x variables with the train_Y_variables
  model_knncv2 = knn.cv(train, traintarget, k=i)
  cv_accuracy2[count] = length(which(model_knncv2==traintarget, T)) / length(model_knncv2)
  count= count+1
}
cv_accuracy2
count=1
for(i in seq(3,11,2))
{
  print(paste("Neighbours=",i, ". Accuracy=",round(cv_accuracy2[count],4)))
  count = count + 1
}
max(cv_accuracy2)
# take the prediction that gives the maximum accuracy
neighbours2= which(cv_accuracy2 == max(cv_accuracy2)) +2
print(paste("optimum neighbours=",neighbours2))

# knn() takes 4 params - Training dataset, Test dataset, Factor(training target), k=<n>
predict_target1 = knn(train, test, traintarget, k=neighbours2)

# create confusion matrix to determine the accuracy
confusionMatrix(as.factor(testtarget), as.factor(predict_target1))

