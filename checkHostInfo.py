#!/usr/bin/env python
#coding:utf-8
#用来查看主机资源使用情况

import requests
import json
import os
import sys



def getinfo():
    f=open('/data/ops/script/checkhost/hostlist','r')
    for line in f.readlines():
        ip=line.strip()
        try:
            df=requests.get('http://%s:1988/page/df'%ip,timeout=5)
            resultdf=json.loads(df.content)
            for i in range(len(resultdf['data'])):
                dir=resultdf['data'][i][5].encode('utf8')
                if dir=='/data':

                    mem=requests.get('http://%s:1988/page/memory'%ip,timeout=5)
                    resultmem=json.loads(mem.content)
                    print ip,resultdf['data'][i][5],"总量:",resultdf['data'][i][1],"剩余:",resultdf['data'][i][3],"使用率:",resultdf['data'][i][4],"总内存:",resultmem['data'][0],"MB","剩余内存:",resultmem['data'][2],"MB"
            
        except  requests.exceptions.Timeout as e:
            print 'http://%s:1988  Timeout'%ip
        except  requests.exceptions.ConnectionError as e:
            print 'http://%s:1988  ConnectionError'%ip

    

if __name__=='__main__':
    getinfo()