#install.packages("RColorBrewer")
#install.packages("rattle")

# decision tree - exercise 1

set.seed(456)
library("rpart")
library("rpart.plot")
library("caret")
library(rattle)
library(RColorBrewer)

#ecoli_file = file.choose()
#col_names = c("type","mcg","gvh","lip","chg","aac","alm1","alm2","lsp")

# signal sequence recognition, signal sequence recognition, Signal Peptidase II consensus sequence score
# Presence of charge on N-terminus of predicted lipoproteins,
# score of discriminant analysis of the amino acid content of outer membrane and periplasmic proteins.
# score of the ALOM membrane spanning region prediction program.
# score of ALOM program after excluding putative cleavable signal regions from the sequence.
path="C:/Users/Danish/Desktop/Data science/decisiontree/ecoli.csv"
ecoli=read.csv(path,header=T)
head(ecoli)
View(ecoli)
table(ecoli$chg)
table(ecoli$lip)
# before carrying out any algorithms, it is essential to understand the dataset very well and remove
# unwanted columns/attributes
# other attributes can be removed gradually as per model building process

ecoli$sequence_name=NULL

levels(factor(ecoli$lsp))
table(ecoli$lsp)
View(ecoli)
# randomly shuffle the dataset
# grp = runif(nrow(ecoli))
# ecoli = ecoli[order(grp),]
ecoli=ecoli[order(sample(1:nrow(ecoli),nrow(ecoli))),]
View(ecoli)
#100*prop.table(table(ecoli$lsp))
#View(ecoli)

# split data into training and test
sample_size=floor(0.7*nrow(ecoli))
sample_ind=sample(seq_len(nrow(ecoli)),sample_size)
train = ecoli[sample_ind,]
test = ecoli[-sample_ind,]
#View(test)
#View(train)
table(train$lsp)
table(ecoli$lsp)
# check the count of Y-classes in
# train and test datasets
length(levels(factor(train$lsp)))
length(levels(factor(test$lsp)))

head(train)
train_x = train[1:7]

# use the decision tree
#basemodel1=rpart(lsp~.,method="class",data=train)
basemodel1=rpart(lsp~.,method="class",data=train, minsplit=5,cp=0.01,maxdepth=5)

# control = reduces CP
basemodel1
summary(basemodel1)
nrow(train)
table(train$lsp)
# complexity parameter
# CP reduces to get more predictions
# CP reduces with every split
# relative error, crossvalidation error, standard error

# relative error reduces with each iteration
# with each gain in information at each split

# std error: distribution error (from mean)

# CV error increases with increase in tree size
# as it depends on the path

# surrogate split:
# if in test data, column is missing, split on the 
# next best column

printcp(basemodel1)

# ?rpart


# remove.packages('rpart.plot')
# remove.packages('rpart')
# remove.packages('rattle')
# remove.packages('RColorBrewer')

# install.packages('rattle')
# install.packages('rpart')
# install.packages('rpart.plot')
# install.packages('RColorBrewer')



# always use rpart.rplot with these parameters to get a good visual output
rpart.plot(basemodel1, type=4, extra=105,
           box.palette = "GnBu",
           branch.lty = 3,
           shadow.col = "gray",
           nn=T)

# node numbering: n(base); 2n and 2n+1
# another chart type

# adjacent mean (for values to split when continuous)
# doesnt work!!!
#fancyRpartPlot(basemodel1,roundint=FALSE)

# count of all Y-variables (check with the graph)
table(train$lsp)

# to find the importance of variables
basemodel1$variable.importance

# predict the ecoli for the test dataset
pdct = predict(basemodel1, test, type="class")
nrow(test)

# get the output in the table for comparison
# Left = Actuals : columns = predictions
table(test$lsp)
table(pdct,test[,8])
confusionMatrix(pdct,test[,8])

table(test[,8],pdct)

prop.table(table(test$lsp))
# NIR -> % of the biggest class (majority class)
# NA could be due to imbalanced classes

# build a new model with the important variables

# COMPLEXITY PARAMETER (CP) - for pruning. Test whether to keep the Decision Tree or Prune it
# find the least cross validated error and prune it
min_cp = basemodel1$cptable[which.min(basemodel1$cptable[,"xerror"]), "CP"]
min_cp

# plot the CP graph to identify pruning
plotcp(basemodel1)

# prune the tree
basemodel1.prune = prune(basemodel1, min_cp)
#dt1.prune = prune(dt1.prune, min_cp)

# plot the pruned tree
windows()
rpart.plot(basemodel1.prune, type=4, extra=101)

# predict with pruned tree
basemodel1.prune = predict(basemodel1.prune, test, type="class")

# create confusion matrix of the pruned prediction
confusionMatrix(test$lsp, basemodel1.prune)
table(test$lsp)  #row is actual data and column is predicted

confusionMatrix(basemodel1.prune,test$lsp)
table(test$lsp)  #column is actual data and row is predicted

# to fix the NA's: try resampling, or combining levels, have more records or have feature selection BUT DO NOT remove these datasets