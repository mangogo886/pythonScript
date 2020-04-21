#!/usr/bin/env python
# coding:utf-8
# 每周巡检脚本
#自动写入excel

import requests
import openpyxl
import json
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def getinfo():
    f = open('/data/ops/script/hostinfo/hosts', 'r')
    wb = openpyxl.load_workbook('/data/ops/script/hostinfo/zhoubao.xlsx')
    sheet = wb.get_sheet_by_name("设备性能记录")
    cpulist = []
    iolist = []
    cpubusylist = []
    percetlist = []
    sysdblist = []
    dblist = []

    for line in f.readlines():
        ip = line.strip()
        try:
            # 获取5分钟负载
            cpuloadcontext = requests.get('http://%s:1988/proc/system/loadavg' % ip, timeout=5)
            cpuload = json.loads(cpuloadcontext.content)['data']['Avg5min']
            cpulist.append(cpuload)

            # sheet['d%s'%num]=cpuload
            # 获取磁盘io
            iocontext = requests.get('http://%s:1988/page/diskio' % ip, timeout=5)
            io = max(json.loads(iocontext.content)['data'])[-1]
            iolist.append(io)

            # cpu使用率
            cpubusycontext = requests.get('http://%s:1988/page/cpu/usage' % ip, timeout=5)
            cpubusy = json.loads(cpubusycontext.content)['data'][0][1]
            cpubusylist.append(cpubusy)

            # 内存剩余百分率
            memfreecontext = requests.get('http://%s:1988/page/memory' % ip, timeout=5)
            freenum = float(json.loads(memfreecontext.content)['data'][2])
            totalnum = float(json.loads(memfreecontext.content)['data'][0])
            freeper = float(format(freenum / totalnum * 100))
            percet = "%.2f%%" % freeper
            percetlist.append(percet)

            # 获取磁盘
            df = requests.get('http://%s:1988/page/df' % ip, timeout=5)
            resultdf = json.loads(df.content)
            # 系统盘剩余
            # print resultdf['data'][0][3]
            # 数据盘
            # print resultdf['data'][1][3]
            sysdblist.append(resultdf['data'][0][3])
            dblist.append(resultdf['data'][1][3])
            print ip, cpuload, io, cpubusy, percet, resultdf['data'][0][3], resultdf['data'][1][3]



        except  requests.exceptions.Timeout as e:
            print 'http://%s:1988  Timeout' % ip
        except  requests.exceptions.ConnectionError as e:
            print 'http://%s:1988  ConnectionError' % ip

    a1 = 5
    for c in cpulist:
        sheet['d%s' % a1] = c
        a1 = a1 + 1
     a2=5
    for i in iolist:
        sheet['e%s' % a2] = i
        a2 = a2 + 1
    a3=5
    for cp in cpubusylist:
        sheet['f%s' % a3] = cp
        a3 = a3 + 1
    a4=5
    for memp in percetlist:
        sheet['j%s' % a4] = memp
        a4 = a4 + 1
    a5=5
    for s in sysdblist:
        sheet['n%s' % a5] = s
        a5 = a5 + 1
    a6=5
    for db in dblist:
        sheet['o%s' % a6] = db
        a6 = a6 + 1
    wb.save('/data/ops/script/hostinfo/zhoubao.xlsx')


if __name__ == '__main__':
    getinfo()