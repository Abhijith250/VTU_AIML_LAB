# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 14:34:47 2022

@author: Abhi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def kernel(point,xmat,k):
    m,n=np.shape(xmat)
    weight=np.mat(np.eye((m)))
    for j in range(m):
       diff=point-x[j]
       weight[j,j]=np.exp(diff*diff.T/-2.0*k**2)
    return weight
def localweight(point,xmat,ymat,k):
     wei=kernel(point,xmat,k)
     w=(x.T*(wei*x)).I*(x.T*(wei*ymat.T))
  
     return w
def localweightedreg(xmat,ymat,k):
    m,n=np.shape(xmat)
    ypred=np.zeros(m)
    for i in range(m):
        ypred[i]=xmat[i]*localweight(xmat[i],xmat,ymat,k)
    return ypred
data=pd.read_csv("lwe.csv")
bill=np.array(data.bill)
tip=np.array(data.tip)
mbill=np.mat(bill)
mtip=np.mat(tip)
m=np.shape(mbill)[1]
ones=np.mat(np.ones(m))
x=np.hstack((ones.T,mbill.T))


ypred=localweightedreg(x,mtip,1)
sortindex=x[:,1].argsort(0)
xsort=x[sortindex][:,0]
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.scatter(bill,tip,color='red')
ax.plot(xsort[:,1],ypred[sortindex])
plt.ylabel("y")
plt.xlabel("x")
plt.show()
        