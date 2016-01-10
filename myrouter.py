#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import sys

class Node:
    def __init__(self,nodeName):
	self.nd = nodeName
	self.childnodes = []

args = sys.argv
startNode = args[1]
endNode = args[2]

imfile = "edges.csv"
f = open(imfile,"r")
edges = csv.reader(f)

def mkway_node(onenode): #ノード作成
	s = Node(onenode)
	for i in edges:
	     if i[1] == onenode or i[2] == onenode:
		     if i[1] == onenode:
		     	s.childnodes.append(i[2])
		     else:
			s.childnodes.append(i[1])
	return s

stnode = mkway_node(startNode) #スタートノードの取得

for i in stnode.childnodes:
	if i == endNode:
		print startNode + "," + i

nxn = []
for nextnode in stnode.childnodes: #スタートノードの次のノードの作成
	nxn.append(mkway_node(nextnode))
	
for k in nxn:
	print k.nd
	for i in k.childnodes:
		print "---" + i

	



