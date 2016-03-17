#!/usr/bin/env python3

import os, ctypes

def info():
	DllName = './a.so'
	if os.path.exists(DllName) == False:
		ret = os.popen('make').readlines()

	so = ctypes.CDLL(DllName)
    func = so.main
    func()

if __name__ == '__main__':
	info()

