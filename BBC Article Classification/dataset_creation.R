install.packages("readtext", dependencies = T)
library(readtext)
rm(list=ls())
setwd('/Users/ankushbharadwaj/Desktop/Github\ Projects/R/bbc\ article\ stuff')
path <- '/Users/ankushbharadwaj/Desktop/Github\ Projects/bbc\ article\ data/bbc'
list_categories <- list.files(path=path)
summary_categories <- data.frame(matrix(ncol=2,nrow=0))
colnames(summary_categories) <- c('Category', 'Number_of_Files')

for (category in list_categories) {
  category_path <- paste(path, category, sep='/')
  n_files <- length(list.files(path=category_path))
  summary_categories = rbind(summary_categories, data.frame('Category'=category, 'Number_of_Files'=n_files))
}

df_final <- data.frame(matrix(ncol=3, nrow=0))
colnames(df_final) <- c('doc_id', 'text', 'category')

for (category in list_categories) {
  category_path <- paste(path, category, sep='/')
  df <- readtext(category_path)
  df['category'] = category
  df_final = rbind(df_final, df)
}

print(list_categories)
print(df_final['category'])
df_w_bad_label <- df_final['category'] == 'README.TXT'
print(sum(df_w_bad_label[,1]))

colnames(df_final) <- c('File_Name','Content','Category')

library(dplyr)
df_final <- 
  df_final %>% 
  mutate(Complete_Filname = paste(File_Name, Category, sep='-'))

save(df_final, file='Dataset.rda')
load(file='Dataset.rda')
class(df_final)
location_of_data <- (paste(path,"News_data.csv",sep='/'))
write.csv2(df_final,location_of_data,row.names= FALSE)
