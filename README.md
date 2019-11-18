# Data-Science-Projects
Collection of data science projects, ranging between personal and educational and research!

[Iris Species Prediction](https://github.com/ankushbharadwaj/Data-Science-Projects/tree/master/Iris%20Species%20Prediction): Tested the accuracy of different machine learning algorithms in predicting the exact species of *Iris* flower based off *Iris* flower data set collected by Edgar Anderson to study the morphologic variation within closely related species of *Iris* flowers. Upon deciding to use the K-Nearest Neighbors algorithm for its accuracy and simplicity, tested the accuracy of my model on the validation set and quantified the model's accuracy for predicting the species of *Iris* based on sepal and petal measurements to be 90%.

***********************************************************

[Loan Prediction](https://github.com/ankushbharadwaj/Data-Science-Projects/tree/master/Loan%20Prediction): Automated processes of a theoretical home loan company by predicting whether or not an individual's loan would be approved by using classification algorithms. Finally settled on using the Random forest algorithm with the predictor variables as follows: Total Income, Loan Amount, Credit History, Dependents, and Property Area. My model, using a Random Forest algorithm, yielded an accuracy of 82.736% and a cross-validation score of 80.297%. 

***********************************************************

[Wine Quality Prediction](https://github.com/ankushbharadwaj/Data-Science-Projects/tree/master/Wine%20Quality%20Prediction): Utilized principal component analysis (PCA) to reduce the variables in a wine quality data set, from this [link](https://archive.ics.uci.edu/ml/datasets/Wine+Quality). After reducing variables to 6 latent variables decided via the aforementioned PCA, used a Naïve Bayes classifier to predict the quality of wine on a test subset of the overall dataset based upon these 6 latent variables. The accuracy I achieved with this model was a relatively low 53.873%. This can be either attributed to the model being inaccurate, or to the fact that wine quality is based arbitrarily on critics' opinions and can't be consistently predicted through objective qualities of the wine. 

***********************************************************

[Boston Home Price Prediction](https://github.com/ankushbharadwaj/Data-Science-Projects/tree/master/Boston%20Home%20Price%20Prediction): Given sample data about 506 homes in Boston and 13 features for each sample, built a linear regression model to predict the price of a house. First, performed regression with only one feature, which in this case was the feature that indicated the number of rooms in a house. The Root Mean Squared Error and R^2 for this regression were 4.9 and .69, respectively. Next, performed a regression using all features, resulting in a Root Mean Squared Error and R^2 of 4.9 and .67, respectively, indicating some benefits of using a regression with just one feature, as this regerssion more accurately fits the data. 

***********************************************************

[BBC Article Classification](https://github.com/ankushbharadwaj/Data-Science-Projects/tree/master/BBC%20Article%20Classification): Downloaded publically available [BBC news article datasets](http://mlg.ucd.ie/datasets/bbc.html) with the intention of deciding on a supervised learning algorithm that can most accurately categorize articles into either 'sport', 'business', 'tech', 'politics', or 'entertainment' when provided with the text of the article, along with gaining valuable insight into factors that differentiate news articles in these categories. 

First, created a dataset with the following features: 'Filename', 'Content', 'Category' through readtext package in [RStudio](https://github.com/ankushbharadwaj/Data-Science-Projects/blob/master/BBC%20Article%20Classification/dataset_creation.R). 'Filename' is the name of the file that contains the news article being observed in that row, 'Content' is the un-parsed text of the news article, and 'Category' is which news category the article belongs to. 

Next, performed [exploratory data analysis and data cleansing](https://github.com/ankushbharadwaj/Data-Science-Projects/blob/master/BBC%20Article%20Classification/EDA_bbc_article.ipynb) by removing "README.TXT" instances, observing percentage distribution of articles by category, as well as distribution of articles by article length, while making adjustments to dataset to bring distributions closer to a normal distribution. 

Most recent action taken on this project is the [feature engineering](https://github.com/ankushbharadwaj/Data-Science-Projects/blob/master/BBC%20Article%20Classification/bbc-articles-featureengineering.ipynb), where the following parsing of the content was done: delete special characters, lowercase all characters, delete punctuation marks, ignore possessive cases, lemmatize the content, and delete English stopwords. Furthermore, category codes were assinged to each different category of news article type and train/test datasets were formed. Finally, elected to use TF-IDF vector representation for text and set the appropriate parameters for the algorithm. 

***********************************************************
