#!/usr/bin/env python
"""
PyMorse  (c) Copyright 2012 Stijn Van Campenhout <stijn.vancampenhout@gmail.com>

Translates morse messages into characters useing de K8055N velleman board
"""
from time import sleep, time
import sys
sys.stdout.softspace = False
from pyk8055 import *
k = k8055(0)
prevVal = ""
startCharTime = ""
pauseTime = time()
endCharTime = ""
curCharMorse = []
morseToChar = {
	".-"	:'A',
	"-..."	:'B',
	"-.-."	:'C',
	"-.."	:'D',
	"."		:'E',
	"..-."	:'F',
	"--."	:'G',
	"...."	:'H',
	".."	:'I',
	".---"	:'J',
	"-.-"	:'K',
	".-.."	:'L',
	"--"	:'M',
	"-."	:'N',
	"---"	:'O',
	'.--.'	:'P',
	"--.-"	:'Q',
	".-."	:'R',
	"..."	:'S',
	"-"		:'T',
	"..-"	:'U',
	"...-"	:'V',
	".--"	:'W',
	"-..-"	:'X',
	"-.--"	:'Y',
	"--.."	:'Z',
	".----"	:'1',
	"..---"	:'2',
	"...--" :'3',
	"....-" :'4',
	"....." :'5',
	"-...."	:'6',
	"--..." :'7',
	"---.." :'8',
	"----."	:'9',
	"-----" :'0',
	'.......':' '
	}
while True:
	curVal = str(k)
	parts = curVal.split(";")
	curVal = parts[0]
	now = time()
	if curCharMorse != []:
		if (now - pauseTime) > 1.00:
			if "".join(curCharMorse) in morseToChar:
				print morseToChar["".join(curCharMorse)] + "(" + "".join(curCharMorse) + ")"
				pauseTime = time()
			curCharMorse = []
	if prevVal != curVal:
		pauseTime = time()
		if curVal == "0":
			if startCharTime != "":
				now = time()
				endCharTime = (now - startCharTime)
				if endCharTime < 0.300:
					curCharMorse.append(".")
				else:
					curCharMorse.append("-")
				startCharTime = ""
			
		else:
			startCharTime = time()

		#print  curVal
		prevVal = curVal

	sleep(0.100)
