#!/usr/bin/env python
#coding:utf-8

from fabric.api import *
from fabric.contrib.files import * 



hostsPath='/data/ops/restart/hostslist'
appPath='/data/ops/restart/rpcapp'

postfix1='-1.0-SNAPSHOT.jar'
postfix0='-0.0.1-SNAPSHOT.jar'

host=file(hostsPath).readlines()
ip_list=[]
for ip in host:
    ip=ip.strip()
    ip_list.append(ip)

env.hosts=ip_list
env.user='ubuntu'
#env.password='qtqky@2018'
env.key_filename="/home/ubuntu/.ssh/id_rsa"



def start():
    path=file(appPath,'r').readlines()
    for dir in path:
        dir = dir.strip()
        rpcname1=dir+postfix1
        rpcname0=dir+postfix0
        app_dir='/data/%s'%dir
        if exists(app_dir):
            with cd(app_dir):
                if exists(rpcname1):
                    run("set -m;nohup java -Xms256m -Xmx512m -jar %s >>nohup.out 2>&1 & echo ok "%rpcname1)
                else:
                    run("set -m;nohup java -Xms256m -Xmx512m -jar %s >>nohup.out 2>&1 & echo ok"%rpcname0)


def stop():
    path=file(appPath,'r').readlines()
    for dir in path:
        dir = dir.strip()
        rpcname1=dir+postfix1
        rpcname0=dir+postfix0
        app_dir='/data/%s'%dir
        if exists(app_dir):
            with cd(app_dir):
                if exists(rpcname1):
                    run("ps -ef|grep %s|grep -v grep|awk '{print $2}'|xargs kill -9"%rpcname1)
                else:
                    run("ps -ef|grep %s|grep -v grep|awk '{print $2}'|xargs kill -9"%rpcname0)