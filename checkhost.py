#!/usr/bin/env python
# coding:utf-8
# 用来查看主机资源使用情况

import requests
import json
import os
import sys
import pandas
import paramiko



def get_javaProcess(ip):
    username='qkyyw'
    privatekey=os.path.expanduser('/home/qkyyw/.ssh/id_rsa')
    key=paramiko.RSAKey.from_private_key_file(privatekey)
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(hostname=ip,username=username,pkey=key)
    cmd="ps -ef|grep java|grep -v grep|wc -l"
    stdin,stdout,stderr=ssh.exec_command(cmd)
    proceCount=stdout.readlines()
    for proc in proceCount:

        return proc.strip('\n')
    ssh.close()
    
   




def getinfo():
    result={}
    iplist=[]
    dirs=[]
    dftotal=[]
    dffree=[]
    dfper=[]
    memtotal=[]
    memfree=[]
    count=[]
    f = open('/data/ops/scripts/hostinfo/hostlist', 'r')
    try:
        for line in f.readlines():
            ip = line.strip()
            df = requests.get('http://%s:1988/page/df' % ip, timeout=5)
            resultdf = json.loads(df.content)
            for i in range(len(resultdf['data'])):
                dir = resultdf['data'][i][5].encode('utf8')
                if dir == '/data':
                    num=get_javaProcess(ip)
                    count.append(num)
                    mem = requests.get('http://%s:1988/page/memory' % ip, timeout=5)
                    resultmem = json.loads(mem.content)
                    iplist.append(ip)
                    dirs.append(resultdf['data'][i][5])
                    dftotal.append(resultdf['data'][i][1])
                    dffree.append(resultdf['data'][i][3])
                    dfper.append(resultdf['data'][i][4])
                    memtotal.append(resultmem['data'][0])
                    memfree.append(resultmem['data'][2])
                    #print ip, resultdf['data'][i][5], "总量:", resultdf['data'][i][1], "剩余:", resultdf['data'][i][3], "使用率:", resultdf['data'][i][4], "总内存:", resultmem['data'][0], "MB", "剩余内存:", resultmem['data'][2], "MB"


    except  requests.exceptions.Timeout as e:
        print 'http://%s:1988  Timeout' % ip
    except  requests.exceptions.ConnectionError as e:
        print 'http://%s:1988  ConnectionError' % ip
    finally:
        pandas.set_option('display.max_columns', 1000)
        pandas.set_option('display.width', 1000)
        pandas.set_option('display.max_colwidth', 1000)
        pandas.set_option('display.unicode.ambiguous_as_wide', True)
        pandas.set_option('display.unicode.east_asian_width', True)
        dict_a = {"IP": pandas.Series(iplist),
              "dir": pandas.Series(dirs),
              "memTotal(MB)": pandas.Series(memtotal),
              "memFree(MB)": pandas.Series(memfree),
              "dfTotal": pandas.Series(dftotal),
              "dfFree": pandas.Series(dffree),
              "dfUsPer": pandas.Series(dfper),
              "javaProceNum":pandas.Series(count)}
        df = pandas.DataFrame(dict_a)
        df=df[["IP","dir","memTotal(MB)","memFree(MB)","dfTotal","dfFree","dfUsPer","javaProceNum"]]
        print pandas.DataFrame(df)

if __name__ == '__main__':
    getinfo()