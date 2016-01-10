#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import sys
import pprint
class Node:
    def __init__(self,nodeName):
	self.nd = nodeName
	self.childnodes = []

args = sys.argv
startNode = args[1]
endNode = args[2]

def mkway_node(onenode): #ノード作成
	imfile = "edges.csv"
	f = open(imfile,"r")
	edges = csv.reader(f)
	s = Node(onenode)
	for edge in edges:
	     if edge[1] == onenode or edge[2] == onenode:
		     if edge[1] == onenode:
		     	s.childnodes.append(edge[2])
		     else:
			s.childnodes.append(edge[1])
	return s

stnode = mkway_node(startNode) #スタートノードの取得

for i in stnode.childnodes:
	if i == endNode:
		print startNode + "," + i

nxn = []
for nextnode in stnode.childnodes: #スタートノードの次のノードの作成
	nxn.append(mkway_node(nextnode))

	
