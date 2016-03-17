#!/usr/bin/env python

import os, ctypes

def info():
	DllName = './a.so'
	if os.path.exists(DllName) == False:
		ret = os.popen('make').readlines()
		print(ret)

	so = ctypes.CDLL(DllName)
	func = so.main
	func()

if __name__ == '__main__':
	info()

