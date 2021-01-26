#!/usr/bin/env python
#coding:utf8

import re
import os
import ConfigParser


def modifyip():

    cf=ConfigParser.ConfigParser()
    cf.read(configPath)
    iplist=cf.sections()    
    for ip in iplist:
        opts=cf.get(ip,'app')
        optsSuffix = opts.split(',')
        for i,suf in enumerate(optsSuffix):
            a=suf.replace('qky-','')
            joinfile=a+filesuffix
            h5file=a+"-h5"+filesuffix
            os.chdir(ngconfig)
            if os.path.exists(joinfile):
                port=httpPort++i+1
                f=open(joinfile,'r')
                context=f.read()
                result=re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9][0-9][0-9][0-9]\b",context)
                if len(result)!=0:
                    oldip=result[0]
                    os.system('sed -i "s/%s/%s:%s/g" %s'%(oldip,ip,port,joinfile))
                    print "%s is replaced by %s:%s in the %s"%(oldip,ip,port,joinfile)
            else:
                print "%s %s does not exist"%(ip,joinfile)

            if os.path.exists(h5file):
                port=httpPort++i+1
                f=open(h5file,'r')
                context=f.read()
                result=re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9][0-9][0-9][0-9]\b",context)
                if len(result)!=0:
                    oldip=result[0]
                    os.system('sed -i "s/%s/%s:%s/g" %s'%(oldip,ip,port,h5file))
                    print "%s is replaced by %s:%s in the %s"%(oldip,ip,port,h5file)
            else:
                print "%s %s does not exist"%(ip,h5file)

           
    f.close()

if __name__=="__main__":
    ngconfig="/data/pythonsrc/sites-available/pro"
    configPath="config.ini"
    filesuffix=".qky100.com.conf"
    httpPort = 8080
    modifyip()