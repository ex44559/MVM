#!/usr/bin/env python

import libvirt
import sys
import os

def shutdownVM( conn, vmlist ):
	for vm in vmlist:
		try:
			dom = conn.lookupByName(vm)
		except:
			print("vm %s not found" % vm)
		else:
			dom.destroy()

if __name__ == '__main__':
	vmlist = sys.argv[1:]
	conn = libvirt.open()
	if conn is None:
		print('Failed to open connection to the hypervisor')
		sys.exit(1)

	shutdownVM(conn, vmlist)