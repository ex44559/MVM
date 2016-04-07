#!/usr/bin/env python

import os
import paramiko
import header

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
	ip_list = header.ip_list
	main(ip_list)
