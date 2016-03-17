#!/usr/bin/env python

import libvirt
import sys
import os

def readXml( path ):
	fp = open(path, 'r')
	xmldesc = fp.read()
	fp.close()

	return xmldesc

def startAllVM( conn, vmlist, path ):
	for vm in vmlist:
		xmlloc = path + vm + '.hvm'
		try:
			dom = conn.lookupByName(vm)
		except:
			xmldesc = readXml(xmlloc)
			dom = conn.createLinux(xmldesc, 0)
			if dom is None:
				print("create vm %s failed" % vm)
			else:
				print("create vm %s sucess" % vm)
		else:
			print("vm %s is running" % vm)


if __name__ == '__main__':
	path = '/home/sunbo/kvm/'
	vmlist = ['vm200', 'vm201', 'vm202', 'vm203']
	conn = libvirt.open()
	if conn is None:
		print('Failed to open connection to the hypervisor')
		sys.exit(1)

	startAllVM(conn, vmlist, path)