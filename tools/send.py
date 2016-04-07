#!/usr/bin/env python

import os
import paramiko
from multiprocessing import Process
import header

def netperf(opfile, ip):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect( ip, 22, username='root', password='123456', timeout=20)

	command = "ps -e | grep netserver && systemctl stop firewalld"
	stdin, stdout, stderr = client.exec_command(command)

	i = 0
	for line in stdout.readlines():
		i += 1

	if i == 0:
		netserver = "netserver"
		stdin, stdout, stderr = client.exec_command(netserver)
		print(ip + ":start netserver")

	for i in range(0, 10):
		command = "netperf -H " + ip
		print("to: " + ip + ":" + command)
		opfile.write(ip+ ":" + command + "\n")
		opfile.write(os.popen(command).read())

	opfile.close()
	client.close()

def main(ip_list):
	r = 0
	plist = []
	for ip in ip_list:
		opfile = open('result'+"%s" % r+'.txt', 'w')
		try:
			p = Process(target = netperf, args = (opfile, ip))
			p.start()
			plist.append(p)
		except Exception, e:
			print("cannot start thread %d" % r)
		r += 1

	if plist != []:
		for pro in plist:
			pro.join()

if __name__ == '__main__':
	ip_list = header.ip_list
	main(ip_list)
