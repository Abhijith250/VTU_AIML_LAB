# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 11:48:30 2022

@author: Abhi
"""
import csv
with open("cd3.csv") as f:
    file=csv.reader(f)
    data=list(file)
   
    s=data[1][:-1]
    print(s)
    g=[["?" for i in range(len(s))] for j in range(len(s))]
    for i in data:
        if i[-1]=="Yes":
            for j in range(len(s)):
                if i[j]!=s[j]:
                    s[j]="?"
                    g[j][j]="?"
        if i[-1]=="No":
            for j in range(len(s)):
                if i[j]!=s[j]:
                    g[j][j]=s[j]
                else:
                    g[j][j]="?"
        print(g)
        print(s)
    gh=[]
    for i in g:
        for j in i:
            if j!="?":
                gh.append(i)
                break
    print("final specific",s)
    print("fianl general",gh)