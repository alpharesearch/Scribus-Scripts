#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random
import scribus

# page size in inch (letter)
pageX = 8.5
pageY = 11.0
lineY = 0.4125
spaceY = 0.1875

scribus.newDocument((pageX, pageY), (0.0, 0.0, 0.0, 0.0), scribus.PORTRAIT, 1, scribus.UNIT_INCHES, scribus.PAGE_1, 0, 1)
scribus.defineColor("lightgray",21,21,21,21)
scribus.defineColor("gray",51,51,51,51)
scribus.defineColor("darkgray",91,91,91,91)

l = scribus.createLine(1.0,0.0,1.0,11)
scribus.setLineColor("gray", l)
l = scribus.createLine(1.05,0.0,1.05,11)
scribus.setLineColor("gray", l)  

for x in range(0,19):
	l = scribus.createLine(0.0,lineY-spaceY,8.5,lineY-spaceY)
	scribus.setLineColor("gray", l) 

	l = scribus.createLine(0.0,lineY,8.5,lineY)
	scribus.setLineColor("lightgray", l)
	scribus.setLineStyle(scribus.LINE_DOT,l) 

	l = scribus.createLine(0.0,lineY+spaceY,8.5,lineY+spaceY)
	scribus.setLineColor("darkgray", l)
	lineY = lineY + 0.5625
