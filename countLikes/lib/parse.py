#!/usr/bin/env python
#title          : parse.py
#description    : Helper Functions for JSON Parsing
#author         : @asinghal 
#=======================================================================================================================

import sys
import requests
import json
import pandas as pd
import csv
from numpy import array

def getDat(url,token):
	"""Loads JSON Data in python friendly format.
	
	url -- Graph API URL
	token -- Access Token. See GRAPH API Documentation to obtain your token
	"""
	param={'access_token': token}
	r=requests.get(url,params=param)
	dat=r.text
	dat=json.loads(dat)
	return dat

def isPage(goal):
	"""Returns True if element specified as Page.

	goal -- Type recorded as input.
	"""
	if goal=='page':
		return True
	else: 
		return False


def getUrl(fbookid, goal):
	"""Transform Facebook ID into the correct GRAPH API format. 
	
	fbookid -- ID of the Element
	goal -- Type of Element. Please see readme for supported elements. 
	"""
	url= 'Invalid entry for "goal" or "id"'
	if isPage(goal):
		url= 'https://graph.facebook.com/%d/?fields=likes' %fbookid
	else:
		url= 'https://graph.facebook.com/%d/likes?summary=1' %fbookid
	return url

def getObjectLikes(json_input):
	"""Returns total Like count for given object JSON.
	
	json_input -- Output JSON of the Graph API call.
	"""
	return json_input['summary']['total_count']

def getPageLikes(json_input):
	"""Returns total Like Count for Type Page.
	
	json_input -- Output JSON of the Graph API call.
	"""
	return json_input['likes']
