# -*- coding: utf-8 -*-

import urllib
import urllib2
import re
from cookielib import CookieJar

reg = re.compile(r'href="\.\/in[^"\\]*(?:\\.[^"\\]*)*"')

stager = re.compile(r'>.+100.')

answers = {1: '/index.php?answer=42', 2: '/index.php?answer=bt'}

wrong = set()

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
response = opener.open("http://maze.qctf.ru/index.php")
content = response.read()

stage = int(stager.findall(content)[0][1:-6])

chosen = answers[1]

response = opener.open("http://maze.qctf.ru"+answers[1])
prev_stage = 1
while True:

	content = response.read()
	stage = int(stager.findall(content)[0][1:-6])
	if stage == prev_stage+1:
		if stage > len(answers):
			print content
			print "Stage "+str(stage)
			print "Success "+str(stage-1)+" with "+chosen
			answers[stage-1] = chosen
	else:
		wrong.add(chosen)
	
	if len(answers) < stage:
		v =  [x[7:-1] for x in reg.findall(content)]
		for x in v:
			if x not in wrong:
				chosen = x
				break
		response = opener.open("http://maze.qctf.ru"+chosen)
	else:
		chosen = answers[stage]
		response = opener.open("http://maze.qctf.ru"+answers[stage])
	prev_stage = stage
