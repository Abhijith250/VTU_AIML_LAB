# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 13:12:58 2022

@author: Abhi
"""

from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv("em.csv")
f1=data['V1'].values
f2=data['V2'].values
x=np.array(list(zip(f1,f2)))
plt.plot(f1,f2,color='black')
plt.show()

kmean=KMeans(3,random_state=0)
label=kmean.fit(x).predict(x)
centroid=kmean.cluster_centers_
plt.scatter(x[:,0],x[:,1],c=label,s=40,cmap='viridis')
plt.scatter(centroid[:,0],centroid[:,1],marker='*',s=200,)
plt.show()

em=GaussianMixture(n_components=3).fit(x)
label=em.predict(x)
proba=em.predict_proba(x)
size=10*proba.max(1)**3
plt.scatter(x[:,0],x[:,1],c=label,s=size)
plt.show()
