#!/usr/bin/env python

import os
import paramiko

def main(ip_list, kill = False):
	for ip in ip_list:
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect( ip, 22, username='root', password='123456', timeout=20)

		command = "ps -e | grep lookbusy"
		stdin, stdout, stderr = client.exec_command(command)
		
		i = 0
		for line in stdout.readlines():
			if kill == True:
				group = line.split()
				pid = group[0]
				cmd = "kill -9 %d" % int(pid)
				stdin, stdout, stderr = client.exec_command(cmd)
				print(ip + ":lookbusy pid %d " % int(pid) + "is killed\n")
			else:
				print(ip + ":lookbusy is running\n")
			i += 1
			
		if i == 0:
			lookbusy = "lookbusy -c 50 -m 2048mb"
			stdin, stdout, stderr = client.exec_command(lookbusy)
			print(ip + ":start lookbusy")


		client.close()


if __name__ == '__main__':
	ip_list = ['192.168.10.200','192.168.10.201','192.168.10.202','192.168.10.203','192.168.10.204'\
	,'192.168.10.205','192.168.10.206','192.168.10.207','192.168.10.208','192.168.10.209'\
	,'192.168.10.210','192.168.10.211','192.168.10.212','192.168.10.213','192.168.10.214',\
	 '192.168.10.215','192.168.10.216'\
	,'192.168.10.217','192.168.10.218','192.168.10.219']
	main(ip_list, True)
