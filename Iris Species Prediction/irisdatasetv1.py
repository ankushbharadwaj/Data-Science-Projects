#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 01:01:38 2019

@author: ankushbharadwaj
"""

## following block of code checks the environment and the version of the library being used
import sys
import scipy
import numpy as np
import matplotlib as mpb
import pandas as pd
import sklearn as sk

print('Python: {}'.format(sys.version))
print('scipy: {}'.format(scipy.__version__))
print('numpy: {}'.format(np.__version__))
print('matplotlib: {}'.format(mpb.__version__))
print('pandas: {}'.format(pd.__version__))
print('sklearn: {}'.format(sk.__version__))

## now, importing all the modules, functions, and objects we will use
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

## now, we're going to load the dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

## summarize data
print(dataset.shape)
print(dataset.head(20))
print(dataset.describe())
print(dataset.groupby('class').size()) ## see class distribution

## visualize data to get a basic idea of the data
    ## univariate plots
        ## box and whisker plots
dataset.plot(kind='box', subplots = True, layout=(2,2), sharex = False, sharey = False)
plt.show()
        ## histogram
dataset.hist()
plt.show() ## histogram shows two input variables w gaussian distribution - sepal-width and sepal-length
    ## multivariate plots
        ## scatterplots
scatter_matrix(dataset)
plt.show()

## let's evaluate algorithms!
    ## first, split out validation dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = .20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X,Y,
    test_size=validation_size, random_state=seed)

## going to use 10-fold cross validation to estimate accuracy
seed = 7
scoring = 'accuracy'

## time to actually build and evaluate the models
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)

## create plot of model evaluation results => compare spread and mean accuracy of each model
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

## see that KNN was pertty accurate, and since it is a very simple agorithm, want to get an idea 
## of the accuracy of model on validation set => final check on accuracy of model
## doing that right here :)
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

