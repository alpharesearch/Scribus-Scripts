#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import scribus

# page size in inch (letter)
pageX = 8.5
pageY = 11
scribus.defineColor("gray",21,21,21,21)

scribus.newDocument((pageX, pageY), (0.0, 0.0, 0.0, 0.0), scribus.LANDSCAPE, 1, scribus.UNIT_INCHES, scribus.PAGE_1, 0, 1)

#0,13 for final
for x in range(0,13):
	#1,12,6 for final
	for y in range(1,12,6):
		rx = x
		ry = y
		for zx in range(0,2):
			for zy in range(0,3):						
				a = scribus.createText(2.25+((zx+0)*(pageX/1.55)), 0.75+(zy*(pageY/3.84)), 1.25, 0.25)
				scribus.setFont('Arial Regular',a)		
				scribus.setFontSize(12, a)
				scribus.setTextColor("gray", a)
				scribus.setTextAlignment(scribus.ALIGN_CENTERED, a)
				scribus.rotateObject(180, a);
				
				rxy = rx-ry
				scribus.insertText('%(rx)d - %(ry)d = %(rxy)d' % locals(), 0, a)		
				
				q = scribus.createText(1.0+((zx+0)*(pageX/1.55)), 1.125+(zy*(pageY/3.84)), 4, 1)
				scribus.setFont('Arial Regular',q)		
				scribus.setFontSize(55, q)
				scribus.setTextAlignment(scribus.ALIGN_CENTERED, q)
				scribus.insertText('%(rx)d + %(ry)d =' % locals(), 0, q)
				ry = ry + 1
		l = scribus.createLine(0.0,2.833333,11,2.833333)
		scribus.setLineColor("gray", l)
		l = scribus.createLine(0.0,5.666666,11,5.666666)
		scribus.setLineColor("gray", l)
		l = scribus.createLine(5.5,0.0,5.5,8.5)
		scribus.setLineColor("gray", l)
		scribus.newPage(-1)
		rx = x
		ry = y
		for zx in range(1,-1,-1):
			for zy in range(0,3):						
				a = scribus.createText(2.25+((zx+0)*(pageX/1.55)), 0.75+(zy*(pageY/3.84)), 1.25, 0.25)
				scribus.setFont('Arial Regular',a)		
				scribus.setFontSize(12, a)
				scribus.setTextColor("gray", a)
				scribus.setTextAlignment(scribus.ALIGN_CENTERED, a)
				scribus.rotateObject(180, a);
				
				rxy = rx+ry
				scribus.insertText('%(rx)d + %(ry)d = %(rxy)d' % locals(), 0, a)		
				
				q = scribus.createText(1.0+((zx+0)*(pageX/1.55)), 1.125+(zy*(pageY/3.84)), 4, 1)
				scribus.setFont('Arial Regular',q)		
				scribus.setFontSize(55, q)
				scribus.setTextAlignment(scribus.ALIGN_CENTERED, q)
				scribus.insertText('%(rx)d - %(ry)d =' % locals(), 0, q)
				ry = ry + 1
#		l = scribus.createLine(0.0,2.833333,11,2.833333)
#		scribus.setLineColor("gray", l)
#		l = scribus.createLine(0.0,5.666666,11,5.666666)
#		scribus.setLineColor("gray", l)
#		l = scribus.createLine(5.5,0.0,5.5,8.5)
#		scribus.setLineColor("gray", l)
		scribus.newPage(-1)	
#	scribus.newPage(-1)
scribus.createLine(0.0,2.833333,11,2.833333)
scribus.createLine(0.0,5.666666,11,5.666666)
scribus.createLine(5.5,0.0,5.5,8.5)
