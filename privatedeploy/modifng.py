#!/usr/bin/env python
#coding:utf-8
#私有云部署更改ng反向代理

import ConfigParser
import os


configPath="config.ini"
ngconfig="/data/privatedep/sites-available/pro"
filesuffix=".qky100.com.conf"
oldip="99.99.99.99:9999"
httpPort = 8080


cf=ConfigParser.ConfigParser()
cf.read(configPath)
iplist=cf.sections()

for ip in iplist:
    opts=cf.get(ip,'app')
    optsSuffix = opts.split(',')
    for i,suf in enumerate(optsSuffix):
        #print ip,i,suf,httpPort++i+1
        a=suf[4:]
        joinfile=a+filesuffix
        os.chdir(ngconfig)
        if os.path.exists(joinfile):
            port=httpPort++i+1
            os.system('sed -i "s/%s/%s:%s/g" %s'%(oldip,ip,port,joinfile))
            print "%s is replaced by %s:%s in the %s"%(oldip,ip,port,joinfile)
        else:
            print "%s %s does not exist"%(ip,joinfile)