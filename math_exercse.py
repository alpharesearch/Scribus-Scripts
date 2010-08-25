#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random
import scribus

# page size in inch (letter)
pageX = 8.5
pageY = 11.0
maxX = 2.0
maxY = 12.0
offsetX = 0.3
offsetXX = 0.2
offsetY = 0.15
minResultA = 0
maxResultA = 14
minResultB = 1
maxResultB = 3
rx = [[0 for col in range(100)] for row in range(100)]
ry = [[0 for col in range(100)] for row in range(100)]

scribus.newDocument((pageX, pageY), (0.0, 0.0, 0.0, 0.0), scribus.PORTRAIT, 1, scribus.UNIT_INCHES, scribus.PAGE_1, 0, 1)
scribus.defineColor("gray",21,21,21,21)

for x in range(0,maxX):
	for y in range(0,maxY):
		q = scribus.createText((x*((pageX*0.9)/maxX))+offsetX, (y*(pageY/maxY))+offsetY, (pageX*0.9)/maxX, pageY/maxY)
		scribus.setFont('Arial Regular',q)
		scribus.setFontSize(48, q)
		if random.randint(0, 1) == 0:
			rx[x][y] = random.randint(minResultB, maxResultB) 
			ry[x][y] = random.randint(minResultA, maxResultA)
		else:
			rx[x][y] = random.randint(minResultA, maxResultA)
			ry[x][y] = random.randint(minResultB, maxResultB)
		rxx = rx[x][y]
		ryy = ry[x][y]
		scribus.insertText('%(rxx)d + %(ryy)d =__' % locals(), 0, q)
scribus.newPage(-1)
xx = 0
for x in range(maxX-1,-1,-1):
	for y in range(0,maxY):
		q = scribus.createText((xx*((pageX/6)/maxX))+offsetXX, (y*(pageY/maxY))+offsetY, (pageX/6)/maxX, pageY/maxY)
		scribus.setFont('Arial Regular',q)
		scribus.setFontSize(20, q)
		scribus.setTextColor("gray", q)
		rr = rx[x][y] + ry[x][y]
#		scribus.setTextAlignment(scribus.ALIGN_CENTERED, q)
		scribus.insertText('%(rr)d' % locals(), 0, q)
	xx+=1

