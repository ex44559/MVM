#!/usr/bin/env python

# using multiprocessing module instead of threading, because
# multiprocessing module supports cmmunication between threads.

import paramiko
import sys
from multiprocessing import Process

def contest(ip, opfile):
	
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	client.connect( ip, 22, username='root', password='123456', timeout=20)
	command = 'netperf -H 192.168.10.188'
	for i in range(0,10):
		print(ip+":"+command)
		stdin, stdout, stderr = client.exec_command(command) 
		opfile.write(ip+ ":" + command + "\n")
		opfile.write(stdout.read())

	client.close()
	opfile.close()
	print(ip+":done!\n")

def concurrency(ip_list):
	i = 0
	plist = []
	for ip in ip_list:
		i+=1
		opfile = open('result'+"%s" % i+'.txt', 'w')
		try:
			p = Process(target = contest, args = (ip, opfile))
			p.start()
			plist.append(p)
		except:
			print ("Error: unable to start thread")
	
	if plist != []:
		for pro in plist:
			pro.join()


if __name__ == '__main__':
	ip_list = ['192.168.10.200','192.168.10.201','192.168.10.202','192.168.10.203','192.168.10.204'\
	,'192.168.10.205','192.168.10.206','192.168.10.207','192.168.10.208','192.168.10.209'\
	,'192.168.10.210','192.168.10.211','192.168.10.212','192.168.10.213','192.168.10.214',\
	 '192.168.10.215','192.168.10.216'\
	,'192.168.10.217','192.168.10.218','192.168.10.219']

	concurrency(ip_list)
