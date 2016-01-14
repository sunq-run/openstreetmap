#!/usr/bin/python

import math
import sys

def near_node(lat,lon):
	radis = 0.0003
	ret = []
	aboutx = float(lat) + radis
	abouty = float(lon) + radis
	aboutx1 = float(lat) - radis
	abouty1 = float(lon) - radis
	f = open("nodepoint.txt","r")
	#print str(aboutx) + ">>>>" + str(aboutx1)
	#print str(abouty) + ">>>>" + str(abouty1)
	for i in f.readlines()[1:-1]:
		wayp = i.split("\t")
	#print str(abouty1) + " <= " + str(wayp[0]) + " <= " + str(abouty) +  " | " +  str(aboutx1)  + " <= " + str(wayp[1]) + " <= " +  str(aboutx) + " " + wayp[3]
		if ((abouty1 <= float(wayp[0])) and (float(wayp[0]) <= abouty)) and ((aboutx1 <= float(wayp[1])) and (float(wayp[1]) <= aboutx)):
			#print wayp[0] + " " + wayp[1] + " " + wayp[3]
			ret.append(wayp[3])
	return ret
	


	



