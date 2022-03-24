# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:32:40 2022

@author: Abhi
"""
def heuristic(v):
    hdist={
        'A':3,
        'B':6,
        'C':4,
        'D':4,
        'E':0
        }
    return hdist[v]

def getneighbors(v):
    if v in graph:
        return graph[v]
    else:
        return None
def astar(start,stop):
    openset=set(start)
    closedset=set()
    g={}
    parent={}
    g[start]=0
    parent[start]=start
    while len(openset)>0:
        n=None
        for v in openset:
            if n==None or g[v]+heuristic(v)<g[n]+heuristic(n):
                n=v
        if n==stop or graph[n]==None:
                pass
        else:
                for (m,weight) in getneighbors(n):
                    if m not in closedset and m not in openset:
                        openset.add(m)
                        parent[m]=n
                        g[m]=g[n]+weight
                    elif g[m]>g[n]+weight:
                        g[m]=g[n]+weight
                        parent[m]=n
                        if m in closedset:
                            closedset.remove(m)
                            openset.add(m)
        if n==None:
                print("No path exist")
                break
        if n==stop:
                path=[]
                while parent[n]!=n:
                    path.append(n)
                    n=parent[n]
                path.append(start)
                path.reverse()
                print(" path is ",path)
                return 
        openset.remove(n)
        closedset.add(n)
    print("No path exist")
    return None
graph={
      'A':[('B',2),('C',4)], 
      'B':[('D',9)],
      'C':[('D',2)],
      'D':[],
      'E':[]
       }
astar('A','D')
astar('A','E')