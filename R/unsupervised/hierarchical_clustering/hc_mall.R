# hierarchical clustering
# dataset: mall data

path="F:/aegis/4 ml/dataset/unsupervised/hierarchical/custmall/1/mallcustomers.csv"
mall=read.csv(path)
View(mall)


# rename columns
colnames(mall)[colnames(mall)=="Annual.Income..k.."]="income"
colnames(mall)[colnames(mall)=="Spending.Score..1.100."]="score"
colnames(mall)

# get only the relevant columns for segmentation
mall1 = mall[,c("income","score")]
head(mall1)

# optimal clusters using dendograms
# method -> minimises variance within each cluster

den = hclust(dist(mall1, method="euclidean"),method="ward.D")
plot(den,main="Dendrogram: Customers",xlab="customers", 
     ylab="distances")

# k=5
opt_k = 5
model=hclust(dist(mall1,method="euclidean"),method="ward.D")
clusters = cutree(model,opt_k)
clusters

# visualise the clusters
clusplot(mall1, clusters, lines=0, shade=T, color=T,
         labels=2,plotchar=F,
         span=F, main="Clusters of Customers",
         xlab="Income", ylab="Score")





