#!/usr/bin/env python

import paramiko
import sys
import readConfig

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
		for i in range(1, repeat)
			stdin, stdout, stderr = client.exec_command(command)
			opfile.write(stdout.read())
		client.close()
	
	opfile.close()	


if __name__ == '__main__':
	measure()
        
        

        