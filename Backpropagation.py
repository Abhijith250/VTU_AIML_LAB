# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 11:17:51 2022

@author: Abhi
"""

import numpy as np
x=np.array(([2, 9], [1, 5], [3, 6]),dtype='float')
y=np.array(([92], [86], [89]),dtype='float')
x=x/np.amax(x,axis=0)
y=y/100

def sigmoid(x):
    return 1/(1+np.exp(-x))
def derative_sig(x):
    return x*(1-x)

epoch=7000
lr=0.1
inp=2
hid=3
op=1

wh=np.random.uniform(size=(inp,hid))
bh=np.random.uniform(size=(1,hid))
wout=np.random.uniform(size=(hid,op))
bout=np.random.uniform(size=(1,op))

for i in range(epoch):
    hinp=np.dot(x,wh)
    hin=hinp+bh
    h_act=sigmoid(hin)
    oinp=np.dot(h_act,wout)
    oin=oinp+bout
    out_act=sigmoid(oin)
    
    
    eo=y-out_act
    ograd=derative_sig(out_act)
    d_output=eo*ograd
    eh=d_output.dot(wout.T)
    hgrad=derative_sig(h_act)
    d_hidden=eh*hgrad
    
    wout+=(h_act.T.dot(d_output))*lr
    wh+=(x.T.dot(d_hidden))*lr
    
print("Input",x)
print("output",y)
print("predicted",out_act)
    
    
    
    
    
    
    
    
    
    
    
    
    
    