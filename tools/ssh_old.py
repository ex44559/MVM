#!/usr/bin/env python

# This file is deprecate, repalced by ssh.py using multiprocessing.

import paramiko
import sys
import readConfig
import thread
import time
import header

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
	print(ip+":done!\n")

def concurrency(ip_list):
	i = 0
	for ip in ip_list:
		i+=1
		opfile = open('result'+"%s" % i+'.txt', 'w')
		try:
			thread.start_new_thread(contest,(ip, opfile))
		except:
			print ("Error: unable to start thread")
		
	time.sleep(600)


if __name__ == '__main__':
	ip_list = header.ip_list
	concurrency(ip_list)
        
        

        
