location <- "/Users/ankushbharadwaj/Desktop/PhenotypeGenotype100SNP50N.csv"
df <- read.csv(location)
df = t(df)
correlation_vector <- vector()
for (i in c(2:nrow(df))){
  model = lm(formula = df[1,] ~ df[i,] -1)
  correlation_vector <- c(correlation_vector, summary(model)$coefficients[1])
}

correlation_vector <- correlation_vector[!is.na(correlation_vector)]
correlated_snps <- data.frame(matrix(ncol = 2, nrow = 10))
for (i in c(1:10)) {
  max_val <- max(correlation_vector)
  max_val_index <- match(max_val, correlation_vector)
  correlated_snps[i,1] <- max_val
  correlated_snps[i,2] <- max_val_index
  correlation_vector <- correlation_vector[correlation_vector != max_val]
}


