# support vector machines

# load the libraries
library(e1071)
library(ggplot2)
library(caret)
library(corrplot) # correlation plot

set.seed(567)
# read the input file
path="C:/Users/Danish/Desktop/Data science/svm/glass.csv"
glass=read.csv(path,header=T)

head(glass)

# remove unwanted columns
# ------------------------
glass$id_number=NULL
str(glass)

# convert the Y-variable to "factor"
# ----------------------------------
glass$Type = as.factor(glass$Type)

# extract the Glass types (Y-variable)
# -------------------------------------
levels(factor(glass$Type))

##################################################

# split the data into numeric and factor variables
# ---------------------

# Do all the numeric check
# ----------------
nums = colnames(glass)[sapply(glass,is.numeric)]
print(nums)

# correlation chart of all X
correl = cor(glass[,nums])
# pairs(correl)

# correlation plot
corrplot(correl,method="number",type="lower")

# returns the position of the columns that are highly collinear given the cutoff value
findCorrelation(correl,cutoff=0.4)
View(correl)

# with more classes, the plot looks more complex and dense
# plot(glass$RI,glass$Na, col=glass$Type)
qplot(glass$RI, glass$Na, color=glass$Type)

# Factor check
# -------------
facts = colnames(glass)[sapply(glass,is.factor)]
print(facts)

# Do all the factors check

# randomly sort the dataset (random uniform distribution)
grp = runif(nrow(glass))
glass = glass[order(grp),]

sampledata = sample(2, nrow(glass), replace=T, prob=c(0.7,0.3) )
train = glass[sampledata==1,]
test = glass[sampledata==2,]
print(paste("Train=",nrow(train),"Test=",nrow(test)))


# There are 4 classification models for SVM
# "linear"for binary,"radial" multiclass,"polynomial"multiclass,"sigmoid"
#binaryclass:c     multiclass: c and y(gamma)
# Build the model here
# --------------------
# This is the Support Vector Machines function

# svm( 
#   factor(Y)~ Xn, 
#   data = <train>, 
#   kernel = "linear", 
#   cost = <COST parameter>, 
#   gamma = <GAMMA parameter>,
#   scale = F
#   )


######################################################
# Function: getOptimalC
# Desc: calculate the optimal C value for a given Kernel
# Return: optimal C
#####################################################
getOptimalC = function(train,K,S)
{
   lis = c(0.001,0.01,0.1,1,5,10,100)
   tune.out = tune(svm, factor(Type)~., 
                   data=train,
                   kernel= K, 
                   ranges = list(cos=lis),
                   scale=S)
   
   C=tune.out$best.parameters[[1]]
   return(C)
}

######################################################
# Function: getOptimalGamma
# Desc: calculate the optimal C value for a given Kernel
# Return: optimal C
#####################################################
getOptimalGamma = function(train,kernel,S)
{
   c_lis = c(0.001,0.01,0.1,1,5,10,100)
   g_lis = c(0.0001,0.001,0.01,0.1,1)
   
   tune.out = tune(svm, factor(Type)~., 
                   data=train,
                   kernel= kernel, 
                   ranges = list(cos=c_lis, 
                                 gamma=g_lis),
                   scale=S)
   
   params=tune.out$best.parameters
   return(params)
}


######################################################
# Function: modelSVM
# Desc: build SVM model for given Kernel/C; predict and output Confusion Matrix
# Return: -
#####################################################
modelSVM = function(train, test,kernel, C,gamma=0.01,s)
{
   model=svm(Type~., data=train, 
             kernel=kernel,
             cost=C, scaled=s)
   
   prediction = predict(model,test)
   
   # confusion matrix
   # ----------------
   
   # in ConfusionMatrix(X,Y),if  
   # X            Y           then  Row         Column
   # ----------   ---------         ----        -------
   # Actual       Predicted         Actual      Predicted
   # Predicted    Actual            Predicted   Actual
   
   cm=confusionMatrix(as.factor(test$Type), as.factor(prediction))
   return(cm)
}


# Build Models with other Kernels
# For each Kernel
#     CV for C, {Gamma}, and Scale = T
#     CV for C, {Gamma}, and Scale = F
# Find the best model that gives the most Accuracy

### 1) SVM model = "linear"
   # scale=F
C=getOptimalC(train,"linear",F); print(C)
modelSVM(train=train,test=test, kernel="linear",C=C,s=F)
table(test$Type)
   # scale=T
C=getOptimalC(train,"linear",T); print(C)
modelSVM(train=train,test=test, kernel="linear",C=C,s=T)

### from here, you need to get the Optimal C and Gamma
### 2) SVM model = "radial"
   # scale=F
ret=getOptimalGamma(train,"radial",F)
C=ret[1]; gamma=ret[2]
modelSVM(train,test,"radial",C,gamma,F)

   # scale=T
ret=getOptimalGamma(train,"radial",T)
C=ret[1]; gamma=ret[2]
modelSVM(train,test,"radial",C,gamma,T)


### 3) SVM model = "polynomial"
   # scale=F
ret=getOptimalGamma(train,"polynomial",F)
C=ret[1]; gamma=ret[2]
modelSVM(train,test,"polynomial",C,gamma,F)

   # scale=T
ret=getOptimalGamma(train,"polynomial",T)
C=ret[1]; gamma=ret[2]
modelSVM(train,test,"polynomial",C,gamma,T)


### 4) SVM model = "sigmoid"
   # scale=F
ret=getOptimalGamma(train,"sigmoid",F)
C=ret[1]; gamma=ret[2]
modelSVM(train,test,"sigmoid",C,gamma,F)

   # scale=T
ret=getOptimalGamma(train,"sigmoid",T)
C=ret[1]; gamma=ret[2]
modelSVM(train,test,"sigmoid",C,gamma,T)
