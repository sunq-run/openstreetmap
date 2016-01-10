#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import sys
import pprint
class Node:
    def __init__(self,nodeName,beforeobj):
	self.nd = nodeName
	self.bobj = beforeobj
	self.childnodes = []

args = sys.argv
startNode = args[1]
endNode = args[2]

def mkway_node(onenode,bobj): #ノード作成
	imfile = "edges.csv"
	f = open(imfile,"r")
	edges = csv.reader(f)
	s = Node(onenode,bobj)
	for edge in edges:
	     if edge[1] == onenode or edge[2] == onenode:
		     if edge[1] == onenode:
		     	s.childnodes.append(edge[2])
		     else:
			s.childnodes.append(edge[1])
	return s

stnode = mkway_node(startNode,"takeyuki") #スタートノードの取得

for i in stnode.childnodes: #スタートノードと終点ノードが同じ、または次のノードである
	if i == endNode:
		print startNode + "," + i + " " + "Goal!"
	if stnode.nd == endNode:
		print "no route :)" 

nxn = [[] for j in range(7)]
for nextnode in stnode.childnodes: #スタートノードの次のノードの作成
	nxn[0].append(mkway_node(nextnode,stnode))

for count in range(5): #階層ルート作成
	for childobj in nxn[count]:
		for nextnode in childobj.childnodes:
			nxn[count+1].append(mkway_node(nextnode,childobj))

def search_st(endidx):
	print endidx.nd + " <-",
	search = endidx.bobj
	for q in range(15):
		if search == "takeyuki":
			continue
		else:
   		   print search.nd + " " + "<-",
		   search = search.bobj
	print "start"
			
def search_end(eN):
	for aindex,a in enumerate(nxn):    #Nodeオブジェクトはnxnに二次元配列として格納している
	    for bindex,b in enumerate(a):
		for c in b.childnodes:
			if c  == eN:
				#print  eN + "あった" + " " + "nxn[" + str(aindex) + "][" + str(bindex) +"]"
				search_st(nxn[aindex][bindex])

search_end(endNode)
