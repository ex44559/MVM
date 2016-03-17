#!/usr/bin/env python

import os, ctypes
import readConfig

def info():
	DllName = './' + readConfig.readConfigDllName()
	if os.path.exists(DllName) == False:
		ret = os.popen('make').readlines()
		print(ret)

	so = ctypes.CDLL(DllName)
	func = so.main
	func()

if __name__ == '__main__':
	info()

