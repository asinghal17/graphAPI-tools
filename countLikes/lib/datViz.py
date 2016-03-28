#!/usr/bin/env python
#title          : datViz.py
#description    : Helper Functions for Visuals
#author         : @asinghal 
#=======================================================================================================================
import sys
import pandas as pd
from numpy import array,arange
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

def getbar(dictionary):
	"""Takes in a dictionary and outputs a Bar Graph of Name and Likes.
	
	dictionary -- Dictionary of Names and their corresponding like_count
	"""
	l=arange(len(dictionary))
	plt.bar(l,dictionary.values(), color='#ff6701', align='center')
	plt.ylabel('# of Likes')
	plt.xticks(l,dictionary.keys())
	plt.xlabel('Name')
	plt.savefig("output/bar.png")
	plt.show()

def getLikesDict(arr):
	"""Takes in a dictionary and outputs a Bar Graph of Name and Likes.
	
	arr -- Array of [Name,ID,Like_Count,Type] 
	"""
	d=dict()
	for item in arr:
		d[item[0]]=item[2]
	return d





