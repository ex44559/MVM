#!/usr/bin/env python

import paramiko
import sys

if __name__ == '__main__':
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect('192.168.10.200', 22, username='root', password='123456', timeout=20)
        stdin, stdout, stderr = client.exec_command('netperf -H 192.168.10.188 -l 30')

        opfile = open('reslut.txt', 'w')
        opfile.write(stdout.read())
        opfile.close()

        client.close