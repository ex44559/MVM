#!/usr/bin/env python

import sys

def fileStatistic(fileList):
	for file in fileList:
		fp = open(file, "r")
		i = 1
		for line in fp.readlines():
			if i % 8 == 0:
				res = line[34:0]
			print(res)

if __name__ == '__main__':
	fileList = ['result1.txt', 'result2.txt', 'result3.txt', 'result4.txt',\
				'result5.txt', 'result6.txt', 'result7.txt', 'result8.txt',\
				'result9.txt', 'result10.txt','result11.txt','result12.txt']
	fileStatistic(fileList)