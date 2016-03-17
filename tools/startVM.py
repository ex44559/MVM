#!/usr/bin/env python

import libvirt
import sys
import os
import startAllVM

if __name__ == '__main__':
	path = '/home/sunbo/kvm/'
	vmlist = sys.argv[1:]
	conn = libvirt.open()
	if conn is None:
		print('Failed to open connection to the hypervisor')
		sys.exit(1)

	startAllVM.startAllVM(conn, vmlist, path)
