#!/usr/bin/env python

import libvirt
import sys
import startAllVM, readConfig

if __name__ == '__main__':
	path = readConfig.readConfigPath()
	vmlist = sys.argv[1:]
	conn = libvirt.open()
	if conn is None:
		print('Failed to open connection to the hypervisor')
		sys.exit(1)

	startAllVM.startAllVM(conn, vmlist, path)
