#!/usr/bin/env python

import paramiko
import sys
import readConfig

def ssh(ip):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	client.connect( ip, 22, username='root', password='123456', timeout=20)
	return client

def measure():
	ip_list = readConfig.readConfigIpList()
	opfile = open('reslut.txt', 'w')

	for ip in ip_list:
		client = ssh(ip)
		stdin, stdout, stderr = client.exec_command('netperf -H 192.168.10.188')
		opfile.write(stdout.read())
		client.close()
	
	opfile.close()	


if __name__ == '__main__':
	measure()
        
        

        