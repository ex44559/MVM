#!/usr/bin/env python

import paramiko
import sys
import readConfig
import thread
import time

def ssh(ip):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	client.connect( ip, 22, username='root', password='123456', timeout=20)
	return client

def measure( repeat = 1, timelen = 10 ):
	ip_list = readConfig.readConfigIpList()
	dest_ip = readConfig.readConfigDestIp()
	opfile = open('reslut.txt', 'w')

	for ip in ip_list:
		client = ssh(ip)
		command = 'netperf -H '+ dest_ip +' -l ' + "%s" % timelen 
		opfile.write(ip+ ":" + command + "\n")
		for i in range(0, repeat):
			print(ip+":"+command)
			stdin, stdout, stderr = client.exec_command(command)
			opfile.write(stdout.read())
		client.close()
	
	opfile.close()	


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

def concurrency():
	ip1 = '192.168.10.200'
	ip2 = '192.168.10.203'

	opfile1 = open('reslut1.txt', 'w')
	opfile2 = open('reslut2.txt', 'w')
	try:
		thread.start_new_thread(contest,(ip1, opfile1))
		thread.start_new_thread(contest,(ip2, opfile2))
	except:
		print ("Error: unable to start thread")
	
	time.sleep(600)


if __name__ == '__main__':
	concurrency()
        
        

        
