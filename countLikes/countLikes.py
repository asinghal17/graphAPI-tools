#!/usr/bin/env python
#title          : countLikes.py
#description    : Take CSV with (Name,Facebook_ID,Type) and outputs a CSV with Total Like Counts using Graph API
#author         : @asinghal 
#=======================================================================================================================
import sys
import pandas as pd
import csv
from numpy import array,arange
from lib.datViz import *
from lib.parse import *

# =================================================
### HELPER FUNCTION
# =================================================

def getLikes(fbookid,token,goal):
	"""Return Like count for a given ID + Type.
	
	fbookid -- Object Facebook ID
	token -- Access Token. See GRAPH API Documentation to obtain your accesstoken.
	goal -- Type of Object. See Readme for supported types.
	"""
	url=getUrl(fbookid, goal)
	json=getDat(url,token)
	if isPage(goal):
		return getPageLikes(json)
	else:
		return getObjectLikes(json)

# =================================================
### LIKE COUNTER
# =================================================

def run_counter(infile,outfile,token):
	"""Takes in a CSV of Facebook IDs and types to give Facebook Like Counts.
	
	infile -- CSV Input. See Readme for Format.
	outfile -- CSV Output.
	"""
	x=pd.read_csv('%s' %infile , delimiter=",")
	arr=array(x)
	cnt=len(arr)
	with open('%s' %outfile, 'a') as h:
		ff = csv.writer(h, delimiter=',')
		for i in arr:
			if cnt<10:
				print "Only %d more left!" %cnt
			name=i[0]
			facebook_id=i[1]
			goal=str(i[2].lower())
			like_cnt=getLikes(facebook_id,token,goal)
			ff.writerow(
				[name,
				 facebook_id,
				 like_cnt,
				 goal])
			cnt-=1


# =================================================
### Main
# =================================================
from argparse import ArgumentParser
parser=ArgumentParser(usage="python countLikes.py input_filename output_filename datViz")
parser.add_argument('infile', help='Input CSV Data File Path')
parser.add_argument('outfile', help='Output CSV File')
parser.add_argument('viz',default="bar", help='Viz Type')
ar=parser.parse_args()

infile='input/'+ar.infile
outfile='output/'+ar.outfile
token=pd.read_csv('input/token.txt')
datViz=ar.viz.lower()

head=(['Name','Facebook_ID', 'Like_Count', 'Type'])

with open(outfile, 'w') as h:
  f = csv.writer(h)
  f.writerow(head)

run_counter(infile,outfile,token)

if datViz=="bar":
	out=pd.read_csv(outfile)
	outarr=array(out)
	out_dict=getLikesDict(outarr)
	getbar(out_dict)
	print ("Thanks for Using countLikes!")
else:
	print ("DatViz not supported/specified!")

