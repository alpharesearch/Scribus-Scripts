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
offsetX = 0.1
offsetXX = 5.5
offsetY = 0.15
maxResult = 25
rx = [[0 for col in range(100)] for row in range(100)]
ry = [[0 for col in range(100)] for row in range(100)]

scribus.newDocument((pageX, pageY), (0.0, 0.0, 0.0, 0.0), scribus.PORTRAIT, 1, scribus.UNIT_INCHES, scribus.PAGE_1, 0, 1)
scribus.defineColor("gray",21,21,21,21)

for x in range(0,maxX):
	for y in range(0,maxY):
		q = scribus.createText((x*(pageX/maxX))+offsetX, (y*(pageY/maxY))+offsetY, pageX/maxX, pageY/maxY)
		scribus.setFont('Arial Regular',q)
		scribus.setFontSize(48, q)
#		scribus.setTextAlignment(scribus.ALIGN_CENTERED, q)
		rx[x][y] = random.randint(0, maxResult)
		ry[x][y] = random.randint(0, (maxResult-rx[x][y]))
		rxx = rx[x][y]
		ryy = ry[x][y]
		scribus.insertText('%(rxx)d + %(ryy)d =__' % locals(), 0, q)
scribus.newPage(-1)
for x in range(0,maxX):
	for y in range(0,maxY):
		q = scribus.createText((x*((pageX/2)/maxX))+offsetXX, (y*(pageY/maxY))+offsetY, (pageX/2)/maxX, pageY/maxY)
		scribus.setFont('Arial Regular',q)
		scribus.setFontSize(20, q)
		scribus.setTextColor("gray", q)
		rr = rx[x][y] + ry[x][y]
#		scribus.setTextAlignment(scribus.ALIGN_CENTERED, q)
		scribus.insertText('%(rr)d' % locals(), 0, q)
