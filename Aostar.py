# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 13:53:06 2022

@author: Abhi
"""

class Graph:
    def __init__(self,graph,heuristicval,start):
        self.graph = graph
        self.H=heuristicval
        self.start = start
        self.parent={}
        self.status={}
        self.solution={}
    def applyaostar(self):
        return self.aostar(self.start,False)
    def getneighbors(self,v):
        return self.graph.get(v,'')
    def getstatus(self,v):
        return self.status.get(v,0)
    def setstatus(self,v,val):
        self.status[v]=val
    def getheuristic(self,v):
        return self.H.get(v,0)
    def setheuristic(self,v,val):
        self.H[v]=val
    def getsolution(self):
        print(self.solution)
    def minimumcostchild(self,v):
        mincost=0
        childnodelist={}
        childnodelist[mincost]=[]
        flag=True
        for child in self.getneighbors(v):
            cost=0
            pathlist=[]
            print(child)
            for c, weight in child:
                cost=cost+self.getheuristic(c)+weight
                pathlist.append(c)
            if flag==True:
                mincost=cost
                childnodelist[mincost]=pathlist
                flag=False
            else:
                if mincost>cost:
                    mincost=cost
                    childnodelist[mincost]=pathlist
        return mincost,childnodelist[mincost]
    def aostar(self,v,back):
        if self.getstatus(v)>=0:
            cost,pathlist=self.minimumcostchild(v)
            self.setstatus(v, len(pathlist))
            self.setheuristic(v, cost)
        solved=True
        for child in pathlist:
            self.parent[child]=v
            if self.getstatus(child)!=-1:
                solved=solved & False
        if solved==True:
            self.setstatus(v, -1)
            self.solution[v]=pathlist
        if v!=self.start:
            self.aostar(self.parent[v], True)
        if not back:
            for child in pathlist:
                self.setstatus(child, 0)
                self.aostar(child,False)

h1 = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J':1, 'T': 3}
graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'C': [[('J', 1)]],
    'D': [[('E', 1), ('F', 1)]],
    'G': [[('I', 1)]]
}
graph1=Graph(graph,h1,'A')
graph1.applyaostar()
graph1.getsolution()


h={'A':3,'B':4,'C':6,'D':9,'E':4,'F':5,'G':1}
graph22={
      'A':[[('B',2),('C',4)],[('D',5)]], 
      'B':[[('E',9)]],
      'C':[[('F',2)]],
      'D':[[('G',9)]],
      'E':[],
      'F':[],
      'G':[]
       }

graph2=Graph(graph22,h,'A')
graph2.applyaostar()
graph2.getsolution()
