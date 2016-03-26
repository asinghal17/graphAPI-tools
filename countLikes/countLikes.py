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
from numpy import array

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
	elif goal=='photo':
		url= 'https://graph.facebook.com/%d/likes?summary=1' %fbookid
	return url

def getPhotoLikes(json_input):
	return json_input['summary']['total_count']

def getPageLikes(json_input):
	return json_input['likes']

def getLikes(fbookid,token,goal):
	url=getUrl(fbookid, goal)
	json= getDat(url,token)
	if goal=='photo':
		return getPhotoLikes(json)
	elif goal=='page':
		return getPageLikes(json)

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
	print ('Success! Please check output directory for result')


# =================================================
### Main
# =================================================
from argparse import ArgumentParser
parser=ArgumentParser(usage="python countLikes.py input_filename output_filename")
parser.add_argument('infile', help='Input CSV Data File Path')
parser.add_argument('outfile', help='Output CSV File')
ar=parser.parse_args()

infile='input/'+ar.infile
outfile='output/'+ar.outfile
token=pd.read_csv('input/token.txt')

head=(['Name','Facebook_ID', 'Like_Count', 'Type'])

with open(outfile, 'w') as h:
  f = csv.writer(h)
  f.writerow(head)

run_counter(infile,outfile,token)
