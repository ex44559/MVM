#!/usr/bin/env python

import ConfigParser
import sys, os, string

def readConfig():
	cf = ConfigParser.ConfigParser()
	cf.read("conf.cfg")
	if cf is None:
		print("Can't read config")
		sys.exit(1)

	return cf

def readConfigPath():
	cf = readConfig()
	return cf.get('settings', 'path')

def readConfigVMList():
	cf = readConfig()
	return cf.get('settings', 'vm_list').split(",")

def readConfigDllName():
	cf = readConfig()
	return cf.get('settings', 'DllName')

if __name__ == '__main__':
	print(readConfigPath())
	print(readConfigVMList())