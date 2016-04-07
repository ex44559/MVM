#!/usr/bin/env python

import os
import paramiko
from multiprocessing import Process

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
		print("to: " + ip + ":" + command)
		opfile.write(ip+ ":" + command + "\n")
		opfile.write(os.popen("netperf -H " + ip).read())

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

if __name__ == '__main__':
	ip_list = ['192.168.10.200','192.168.10.201','192.168.10.202','192.168.10.203','192.168.10.204'\
	,'192.168.10.205','192.168.10.206','192.168.10.207','192.168.10.208','192.168.10.209'\
	,'192.168.10.210','192.168.10.211','192.168.10.212','192.168.10.213','192.168.10.214',\
	 '192.168.10.215','192.168.10.216'\
	,'192.168.10.217','192.168.10.218','192.168.10.219']
	main(ip_list)
