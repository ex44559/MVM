#!/usr/bin/env python

import libvirt
import sys
import os

def shutdownAllVM():
	conn = libvirt.open()
	if conn is None:
		print('Failed to open connection to the hypervisor')
		sys.exit(1)

	for vm in conn.listDomainsID():
		try:
			dom = conn.lookupByID(vm)
		except libvirt.libvirtError:
			print ("vm %s not found" % vm)
		else:
			dom.destroy()

if __name__ == '__main__':
	shutdownAllVM()