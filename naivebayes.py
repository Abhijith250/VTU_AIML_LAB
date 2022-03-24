# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:09:07 2022

@author: Abhi
"""



from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import numpy
data=pd.read_csv("naivtext.csv",names=['message','label'])
data['labelnum']=data.label.map({'pos':1,'neg':0})
x=data.message
y=data.labelnum

x_train,x_test,y_train,y_test=train_test_split(x,y)

cv=CountVectorizer()
x_train_dtm=cv.fit_transform(x_train)
x_test_dtm=cv.transform(x_test)



df=pd.DataFrame(x_train_dtm.toarray(),columns=cv.get_feature_names())
print(df[0:5])
model=MultinomialNB()
print(x_train_dtm.shape,y_train.shape)
model.fit(x_train_dtm,y_train)
pred=model.predict(x_test_dtm)

from sklearn import metrics
print(metrics.accuracy_score(y_test,pred))
print(metrics.precision_score(y_test,pred))
print(metrics.recall_score(y_test,pred))
print(metrics.confusion_matrix(y_test,pred))
print(metrics.classification_report(y_test,pred))


