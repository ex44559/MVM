#!/usr/bin/env python

import os
import paramiko

def main(ip_list):
	
	for ip in ip_list:
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect( ip, 22, username='root', password='123456', timeout=20)
		
		sftp = client.open_sftp()
		remote_flie = sftp.file("/home/sunbo/lookbusy-1.4.tar.gz", "wb")
		remote_flie.set_pipelined(True)
		tar = open("lookbusy-1.4.tar.gz", "r")
		remote_flie.write(tar.read())
		sftp.close()
		tar.close()

		make = "cd /home/sunbo/ && tar xzf lookbusy-1.4.tar.gz &&\
			cd lookbusy-1.4 && ./configure && make && make install"
		stdin, stdout, stderr = client.exec_command(make)
		print(stdout.read())

		client.close()

if __name__ == '__main__':
	ip_list = ['192.168.10.200','192.168.10.201','192.168.10.202','192.168.10.203','192.168.10.204'\
		,'192.168.10.205','192.168.10.206','192.168.10.207','192.168.10.208','192.168.10.209'\
		,'192.168.10.210','192.168.10.211']
	main(ip_list)
