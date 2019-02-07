#!/bin/usr/env python3

import os
import urllib.request
import sys
import re

# Precondition: url is a string
# Postcondition: the html for url is returned as an array, with one line per index
def getHTML(url):
	html=[]

	# check if url is in a valid format
	try:
		req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 Windows NT 6.1; Win64; x64)'}) # set client as firefox
	except ValueError:
		print(url+' is not in a valid URL format!')
		sys.exit()

	# check if url is live
	try:
		response=urllib.request.urlopen(req) # get response form req
	except urllib.error.URLError:
		print(url+' is not a live url!')
		sys.exit()

	for line in response:
		html.append(line.decode().strip('\n')) # convert to string from byte array and strip endlines

	return html


# Precondition: html is an array of strings, search_string is a string which can include regular expressions
# Postcondition: an array of lines containing search criteria
def searchHTML(html, searchString0, searchString1=''):
	parsedLines=[]
	pattern=re.compile(searchString0)

	for line in html:
		if (searchString1!=''):
			if (line.find(searchString0)>-1 and line.find(searchString1)>-1):
				parsedLines.append(line)

		else:
			if (pattern.search(line)!=None):
				parsedLines.append(line)

	return parsedLines


# Precondition: lines as an array of strings, start is the beginning of the substring, end is the end of the substring, start_offset is the offset from start, end_offset is the offset from the end
# Postcondition: an array of the parsed lines as strings
def parseString(lines, start, end, startOffset=0, endOffset=0):
	parsedLines=[]

	for line in lines:
		parsedLine=line[line.find(start)+startOffset:line.find(end)+endOffset]
		if (parsedLine!=''):
			parsedLines.append(parsedLine)

	return parsedLines


# Don't judge me!
def parseJSON(JSON):
	index=0
	line=''
	parsedJSON=[]
	JSONDataObjs=[]
	objValues={}
	darkSkyHours=[]
	started=False
	index=0
	flag=0

	for s in str(JSON):
		line+=s
		if (s=='[' or s==']'):
			index+=1
			parsedJSON.append(line)
			line=''
		elif (s=='{' or s=='}'):
			index+=1
			parsedJSON.append(line)
			line=''
		elif (s==','):
			index+=1
			parsedJSON.append(line)
			line=''

	for a in parsedJSON:
		if (a=='"data":['):
			flag=1
			JSONDataObjs.append(a)
		elif (a==']' and flag==1):
			flag=0
			JSONDataObjs.append(a)
		elif(flag==1):
			JSONDataObjs.append(a)
		else:
			pass

	for b in JSONDataObjs:
		if (b=='{'):
			started=True
		elif (b.find('}')>=1):
			started=False
			objValues[b[1:b.find(':')-1]]=b[b.find(':')+1:b.find('}')-1]
			darkSkyHours.append(objValues)
			objValues={}
		elif (started==True):
			objValues[b[1:b.find(':')-1]]=b[b.find(':')+1:len(b)-1]

	return darkSkyHours
