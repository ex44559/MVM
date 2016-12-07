#!/usr/bin/env python

import libvirt
import sys
import readConfig

def readXml( path ):
	fp = open(path, 'r')
	xmldesc = fp.read()
	fp.close()

	return xmldesc

def start( vm ):
	xmlloc = path + vm + '.hvm'
	xmldesc = readXml(xmlloc)
	dom = conn.createLinux(xmldesc, 0)
	if dom is None:
		print("create vm %s failed" % vm)
	else:
		print("create vm %s sucess" % vm)

def startlist( conn, vmlist, path ):
	for vm in vmlist:
		try:
			dom = conn.lookupByName(vm)
		except:
			start(vm)
			continue
		
		if dom == None:
			start(vm)
		else:
			print("vm %s is running" % vm)


if __name__ == '__main__':
	path = readConfig.readConfigPath()
	vmlist = readConfig.readConfigVMList()
	conn = libvirt.open()
	if conn is None:
		print('Failed to open connection to the hypervisor')
		sys.exit(1)

	startlist(conn, vmlist, path)
