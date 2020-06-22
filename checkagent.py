#!/usr/bin/env python

#coding:utf-8
#定期检查agent状态，实现agent自动重启

import paramiko
import os
import sys
reload(sys)
sys.setdefaultencoding("utf8")


hosts=['web1','video1']

def checkAgent():
    username='zjyw'
    privatekey=os.path.expanduser('/home/zjyw/.ssh/id_rsa')
    key=paramiko.RSAKey.from_private_key_file(privatekey)
    for host in hosts:
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.connect(hostname=host,username=username,pkey=key)

        chechdir="ls -all /data/ops/falcon-agent/open-falcon"
        cmd1="netstat -nultp|grep 1988"
        restartagnet="cd /data/ops/falcon-agent;./open-falcon restart agent"
        stdin,stdout,stderr=ssh.exec_command(chechdir)
		#这里读取stderr，如果无错误，则判断目录存在，因为如果使用stdout，可能遇到gbk字符不兼容报错
        dirs=stderr.readlines()
        stdin,stdout,stderr=ssh.exec_command(cmd1)
        agentport=stdout.readlines()

        if len(dirs)==0:
            if len(agentport)==0:
                stdin,stdout,stderr=ssh.exec_command(restartagnet)
                print host,stdout.readlines()
            else:
                print host,"falcon-agnent is running"
        else:
            print host,"/data/ops/falcon-agent/open-falcon not exist"
    ssh.close()


checkAgent()