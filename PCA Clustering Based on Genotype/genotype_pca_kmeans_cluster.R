location <- "/Users/ankushbharadwaj/Desktop/Genotype40kSNP50N.txt"
df <- read.table(location, header=FALSE, sep = " ")

df <- t(df)

library('ggfortify')

pca = prcomp(df,retx=T)
plot(pca)
plot(pca_mod$x[,1],pca_mod$x[,2], xlab="PC1", ylab="PC2", main="PC1 VS PC2", type="p")

comp <- data.frame(pca$x[,1:2])
k <- kmeans(comp, 2, nstart=25, iter.max=1000)
plot(comp, col=k$clust, pch=16)
