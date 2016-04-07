#!/usr/bin/env python

import sys
import header

def fileStatistic(fileList):
	output = open("summary.txt", "w")
	for file in fileList:
		output.write(file + "\n")
		fp = open(file, "r")
		i = 1
		for line in fp.readlines():
			if i % 8 == 0:
				res = line[33:]
				output.write(res)
			i+=1
		fp.close()
	output.close()

if __name__ == '__main__':
	fileList = header.fileList
	
	fileStatistic(fileList)
