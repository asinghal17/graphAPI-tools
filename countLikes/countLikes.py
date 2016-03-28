#!/usr/bin/env python
#title          : countLikes.py
#description    : Take CSV with (Name,Facebook_ID,Type(Picture,Page)) and outputs a CSV with Total Like Counts using Graph API
#author         : @asinghal 
#=======================================================================================================================

import sys
import requests
import json
import pandas as pd
import csv
from numpy import array,arange
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
# =================================================
### Helper Functions
# =================================================

def getDat(url,token):
	param={'access_token': token}
	r=requests.get(url,params=param)
	dat=r.text
	dat=json.loads(dat)
	return dat

def getUrl(fbookid, goal):
	url= 'Invalid entry for "goal" or "id"'
	if goal=='page':
		url= 'https://graph.facebook.com/%d/?fields=likes' %fbookid
	else:
		url= 'https://graph.facebook.com/%d/likes?summary=1' %fbookid
	return url

def getObjectLikes(json_input):
	return json_input['summary']['total_count']

def getPageLikes(json_input):
	return json_input['likes']

def getLikes(fbookid,token,goal):
	url=getUrl(fbookid, goal)
	json= getDat(url,token)
	if goal=='page':
		return getPageLikes(json)
	else:
		return getObjectLikes(json)

def getbar(dictionary):
	l=arange(len(dictionary))
	plt.bar(l,dictionary.values(), color='#ff6701', align='center')
	plt.ylabel('# of Likes')
	plt.xticks(l,dictionary.keys())
	plt.xlabel('Name')
	plt.savefig("output/bar.png")
	plt.show()

def getLikesDict(arr):
	d=dict()
	for item in arr:
		d[item[0]]=item[2]
	return d

# =================================================
### LIKE COUNTER
# =================================================

def run_counter(infile,outfile,token):
	"""Takes in a CSV of Facebook IDs and types to give Facebook Like Counts.
	
	infile -- CSV Input (Facebook_ID, Type)
	outfile -- CSV Output of (Facebook_ID,Like Counts,Type)
	"""
	x=pd.read_csv('%s' %infile , delimiter=",")
	arr=array(x)
	cnt=len(arr)
	with open('%s' %outfile, 'a') as h:
		ff = csv.writer(h, delimiter=',')
		for i in arr:
			if cnt<5:
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
parser=ArgumentParser(usage="python countLikes.py input_filename output_filename [--viz]")
parser.add_argument('infile', help='Input CSV Data File Path')
parser.add_argument('outfile', help='Output CSV File')
parser.add_argument('viz',default="None", help='Viz Type')
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
else:
	print ("Viz " + datViz + " Not Supported")

