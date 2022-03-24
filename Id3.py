# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:47:46 2022

@author: Abhi
"""

from pprint import pprint
import math
from collections import Counter
import pandas as pd

df=pd.read_csv("id3dataset.csv")

def entropy(probs):
    return sum([-prob*math.log(prob,2) for prob in probs])
def entropylist(a_list):
    cnt=Counter(x for x in a_list)
    num=len(df)*1.0
    probs=[x/num for x in cnt.values()]
    return entropy(probs)
def infogain(df,splitattribute,target,trace=0):
    df_split=df.groupby(splitattribute)
    for name,group in df_split:
        print(name)
        print(group)
    nobs=len(df.index)*1.0
    df_agent=df_split.agg({target:[entropylist,lambda x:len(x)/nobs]})[target]
    df_agent.columns=['entropy','propobservation']
    new=sum(df_agent['entropy']*df_agent['propobservation'])
    old=entropylist(df[target])
    return old-new

print(infogain(df,'Age','profit'))
def id3(df,target,attribute_names,default_class=None):
    print(df['profit'])
    print(df[target])
    cnt=Counter(x for x in df[target])
    if len(cnt)==1:
        return next(iter(cnt))
    elif df.empty or (not attribute_names):
        return default_class
    else:
        default_class=max(cnt.keys())
        gainz=[infogain(df,attr,target) for attr in attribute_names]
        indexbest=gainz.index(max(gainz))
        bestattr=attribute_names[indexbest]
        tree={bestattr:{}}
        rem=[i for i in attribute_names if i!=bestattr]
        for val, datasub in df.groupby(bestattr):
            subset=id3(datasub,target,rem,default_class)
            tree[bestattr][val]=subset
        return tree
    
columns=list(df.columns)
print(columns)
columns.remove('profit')
print(columns)
tree=id3(df,'profit',columns)
pprint(tree)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    