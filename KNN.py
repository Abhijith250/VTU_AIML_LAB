# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:53:17 2022

@author: Abhi
"""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import datasets

iris=datasets.load_iris()
iris_data=iris.data
iris_label=iris.target

print(iris_data,iris_label)
print(iris.target_names)

x_train,x_test,y_train,y_test=train_test_split(iris_data,iris_label,test_size=0.30)
model=KNeighborsClassifier()
model.fit(x_train,y_train)
pred=model.predict(x_test)

from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,pred))
print(confusion_matrix(y_test,pred))