#!/usr/bin/env python
#coding:utf-8
#用来查看金山云正式环境主机资源使用情况

import requests
import json
import MySQLdb
import os
import sys



def getinfo():
    con = MySQLdb.connect(host='', user='openFalcon', passwd='Daef=596', db='falcon_portal',charset="utf8")
    cursor = con.cursor()
    sql = "SELECT ip FROM `host` where  hostname like '%pro%' and ip like '10%';"
    cursor.execute(sql)
    host = cursor.fetchall()
    hosts = list(host)
    for ip in hosts:
        try:
            df=requests.get('http://%s:port/page/df'%ip,timeout=5)
            resultdf=json.loads(df.content)
            temp_ip=eval(json.dumps(ip))[0]
            for i in range(len(resultdf['data'])):
                dir=resultdf['data'][i][5].encode('utf8')
                if dir=='/data':

                    mem=requests.get('http://%s:port/page/memory'%ip,timeout=5)
                    resultmem=json.loads(mem.content)
                    print temp_ip,resultdf['data'][i][5],"总量:",resultdf['data'][i][1],"剩余:",resultdf['data'][i][3],"使用率:",resultdf['data'][i][4],"总内存:",resultmem['data'][0],"MB","剩余内存:",resultmem['data'][2],"MB"
            
        except  requests.exceptions.Timeout as e:
            print 'http://%s:port  Timeout'%ip
        except  requests.exceptions.ConnectionError as e:
            print 'http://%s:port  ConnectionError'%ip

    cursor.close()
    con.close()

if __name__=='__main__':
    getinfo()