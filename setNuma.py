#!/usr/bin/env python

import libvirt
import sys
import os

def setNuma(conn, vm, NumaPolicy):
	try:
		dom = conn.lookupByName(vm)
	except:
		print("vm %s not found" % vm)
	else:
		dom.setNumaParameters(NumaPolicy)


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("two arguments")
		sys.exit(0)

	#if allow all numa node, set numa_nodeset: 0-n, n is the number of numa nodes
	NumaPolicy = {'numa_nodeset': '0', 'numa_mode': 0}
	vm = sys.argv[1]
	NumaPolicy['numa_nodeset'] = sys.argv[2]

	conn = libvirt.open()
	if conn is None:
		print('Failed to open connection to the hypervisor')
		sys.exit(1)

	setNuma(conn, vm, NumaPolicy)
