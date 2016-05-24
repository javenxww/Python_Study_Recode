#!/usr/bin/python3
# -*- coding:utf8 -*-
import paramiko
server = {'servername':['ip',port,'user','password']}   #change it as your own ssh account

def Reboot_VPS(server_name):
	server_account = server[server_name]
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(*server_account)
		stdin,stdout,stderr = ssh.exec_command('uname -a')
		system_info = ' ' + str(stdout.read(),encoding='utf8')
		stdin,stdout,stderr = ssh.exec_command('head -n 1 /etc/issue')
		OS_info = ' '.join(str(stdout.read(),encoding='utf8').split())
		print('***********************************************')
		print(system_info,OS_info)
		stdin,stdout,stderr = ssh.exec_command('reboot')
		print(' %s Reboot'%server_name)
		print('***********************************************')
	except TimeoutError as e:
		print('***********************************************')
		print(' %s connect ERROR'%server_name)
		print('***********************************************')




if __name__ == "__main__":
	Reboot_VPS('servername')  #change it as your own server name