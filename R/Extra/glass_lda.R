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
tot=nrow(glass)
s=sample(seq(1,tot),0.7*tot)
train=glass[s,]
test=glass[-s,]
print(paste("Train ",nrow(train),"Test ",nrow(test)))

train$Type=as.factor(train$Type)
test$Type=as.factor(test$Type)

table(train$Type)
table(test$Type)
#build the LDA model with all features
mod1=lda(Type~.,data=train)
mod1

pred1=predict(mod1,test)$class
confusionMatrix(test$Type,pred1) 
