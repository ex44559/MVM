#!/usr/bin/env python

import sys

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
	fileList = ['result1.txt', 'result2.txt', 'result3.txt', 'result4.txt',\
				'result5.txt', 'result6.txt', 'result7.txt', 'result8.txt',\
				'result9.txt', 'result10.txt','result11.txt','result12.txt',\
				'result13.txt', 'result14.txt','result15.txt','result16.txt',
				'result17.txt','result18.txt','result19.txt']
	fileStatistic(fileList)
