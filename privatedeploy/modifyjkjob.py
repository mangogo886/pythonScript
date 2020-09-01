#!/usr/bin/env python
#coding:utf8
#批量修改jk job主机

import os
import glob
import xml.etree.ElementTree as ET
import ConfigParser




#前端
def fewritexml():
    for dirpath in frontendpath:
        filepath=dirpath+configfile
        if os.path.exists(filepath):
            tree = ET.parse(filepath)
            root = tree.getroot()
            host=root.find('buildWrappers').find('jenkins.plugins.publish__over__ssh.BapSshPostBuildWrapper').find('postBuild').find('delegate').find('publishers').find('jenkins.plugins.publish__over__ssh.BapSshPublisher').find('configName')
            command=root.find('buildWrappers').find('jenkins.plugins.publish__over__ssh.BapSshPostBuildWrapper').find('postBuild').find('delegate').find('publishers').find('jenkins.plugins.publish__over__ssh.BapSshPublisher').find('transfers').find('jenkins.plugins.publish__over__ssh.BapSshTransfer').find('execCommand').text

            host.text=fehost
            tree.write(filepath)
            print "修改PC前端job ",filepath,"部署主机为 ",fehost



#h5
def h5writexml():
    for dirpath in h5path:
        filepath=dirpath+configfile
        if os.path.exists(filepath):
            tree = ET.parse(filepath)
            root = tree.getroot()
            host=root.find('buildWrappers').find('jenkins.plugins.publish__over__ssh.BapSshPostBuildWrapper').find('postBuild').find('delegate').find('publishers').find('jenkins.plugins.publish__over__ssh.BapSshPublisher').find('configName')
            command=root.find('buildWrappers').find('jenkins.plugins.publish__over__ssh.BapSshPostBuildWrapper').find('postBuild').find('delegate').find('publishers').find('jenkins.plugins.publish__over__ssh.BapSshPublisher').find('transfers').find('jenkins.plugins.publish__over__ssh.BapSshTransfer').find('execCommand').text

            host.text=fehost
            tree.write(filepath)
            print "修改h5前端job ",filepath,"部署主机为 ",fehost




#后端
def bewritexml():
    cf=ConfigParser.ConfigParser()
    cf.read(configPath)
    hostlist=cf.sections()
    for host in hostlist:
        applist=cf.get(host,'app').split(',')
        for ap in applist:
            #拼接后端config.xml，并判断
            jobspathbe=commondir+ap+bksuffix+"/"+configfile
            if os.path.exists(jobspathbe):
                tree = ET.parse(jobspathbe)
                root = tree.getroot()
                hostname=root.find('buildWrappers').find('jenkins.plugins.publish__over__ssh.BapSshPostBuildWrapper').find('postBuild').find('delegate').find('publishers').find('jenkins.plugins.publish__over__ssh.BapSshPublisher').find('configName')
                hostname.text=host
                print hostname.text
                tree.write(jobspathbe)
                print "修改jobs %s 文件 "%(ap+bksuffix),jobspathbe,"部署主机为 ",host

            else:
                print jobspathbe,"job文件不存在"


#RPC
def rpcwritexml():
    cf=ConfigParser.ConfigParser()
    cf.read(configPath)
    hostlist=cf.sections()
    for host in hostlist:
        applist=cf.get(host,'app').split(',')
        for ap in applist:
            #拼接RPC的config.xml，并判断
            jobspathrpc=commondir+ap+rpcsuffix+"/"+configfile
            if os.path.exists(jobspathrpc):
                tree = ET.parse(jobspathrpc)
                root = tree.getroot()
                hostname=root.find('buildWrappers').find('jenkins.plugins.publish__over__ssh.BapSshPostBuildWrapper').find('postBuild').find('delegate').find('publishers').find('jenkins.plugins.publish__over__ssh.BapSshPublisher').find('configName')
                hostname.text=host
                tree.write(jobspathrpc)
                print "修改jobs %s 文件 "%(ap+rpcsuffix),jobspathrpc,"部署主机为 ",host
            else:
                print jobspathrpc,"job文件不存在"


#--------------------------修改command部分。根据需要启用，默认不跑以下函数--------------------

#修改前端command
def modifycommandfe():
    old=raw_input("输入原内容: ")
    new=raw_input("输入替换后内容: ")
    for dirpath in frontendpath:
        filepath=dirpath+configfile
        if os.path.exists(filepath):
            tree = ET.parse(filepath)
            root = tree.getroot()
            command=root.find('buildWrappers').find('jenkins.plugins.publish__over__ssh.BapSshPostBuildWrapper').find('postBuild').find('delegate').find('publishers').find('jenkins.plugins.publish__over__ssh.BapSshPublisher').find('transfers').find('jenkins.plugins.publish__over__ssh.BapSshTransfer').find('execCommand')
            newcommand=command.text.replace(old,new)
            command.text=newcommand
            tree.write(filepath)
            print "%s 替换 %s %s"%(new,old,filepath)


#修改H5端command
def modifycommandh5():
    old=raw_input("输入原内容: ")
    new=raw_input("输入替换后内容: ")
    for dirpath in h5path:
        filepath=dirpath+configfile
        if os.path.exists(filepath):
            tree = ET.parse(filepath)
            root = tree.getroot()
            command=root.find('buildWrappers').find('jenkins.plugins.publish__over__ssh.BapSshPostBuildWrapper').find('postBuild').find('delegate').find('publishers').find('jenkins.plugins.publish__over__ssh.BapSshPublisher').find('transfers').find('jenkins.plugins.publish__over__ssh.BapSshTransfer').find('execCommand')
            newcommand=command.text.replace(old,new)
            command.text=newcommand
            tree.write(filepath)
            print "%s 替换 %s %s"%(new,old,filepath)



#修改后端command
def modifycommandbe():
    old=raw_input("输入原内容: ")
    new=raw_input("输入替换后内容: ")
    cf=ConfigParser.ConfigParser()
    cf.read(configPath)
    hostlist=cf.sections()
    for host in hostlist:
        applist=cf.get(host,'app').split(',')
        for ap in applist:
            #拼接后端config.xml，并判断
            jobspathbe=commondir+ap+bksuffix+"/"+configfile
            if os.path.exists(jobspathbe):
                tree = ET.parse(jobspathbe)
                root = tree.getroot()
                command=root.find('buildWrappers').find('jenkins.plugins.publish__over__ssh.BapSshPostBuildWrapper').find('postBuild').find('delegate').find('publishers').find('jenkins.plugins.publish__over__ssh.BapSshPublisher').find('transfers').find('jenkins.plugins.publish__over__ssh.BapSshTransfer').find('execCommand')
                newcommand=command.text.replace(old,new)
                command.text=newcommand
                tree.write(jobspathbe)
                print "%s 替换 %s %s"%(new,old,jobspathbe)


#修改RPC的command
def modifycommandrpc():
    old=raw_input("输入原内容: ")
    new=raw_input("输入替换后内容: ")
    cf=ConfigParser.ConfigParser()
    cf.read(configPath)
    hostlist=cf.sections()
    for host in hostlist:
        applist=cf.get(host,'app').split(',')
        for ap in applist:
            #拼接RPC的config.xml，并判断
            jobspathrpc=commondir+ap+rpcsuffix+"/"+configfile
            if os.path.exists(jobspathrpc):
                tree = ET.parse(jobspathrpc)
                root = tree.getroot()
                command=root.find('buildWrappers').find('jenkins.plugins.publish__over__ssh.BapSshPostBuildWrapper').find('postBuild').find('delegate').find('publishers').find('jenkins.plugins.publish__over__ssh.BapSshPublisher').find('transfers').find('jenkins.plugins.publish__over__ssh.BapSshTransfer').find('execCommand')
                newcommand=command.text.replace(old,new)
                command.text=newcommand
                tree.write(jobspathrpc)
                print "%s 替换 %s %s"%(new,old,jobspathrpc)





if __name__=="__main__":
    frontendpath=glob.glob("/data/.jenkins/jobs/qky-*-frontend/")
    h5path=glob.glob("/data/.jenkins/jobs/qky-*-h5/")
    commondir="/data/.jenkins/jobs/"
    bksuffix="-backend"
    rpcsuffix="-service"
    configfile="config.xml"
    configPath="config.ini"
    fehost="ng01"

    fewritexml()
    h5writexml()
    bewritexml()
    rpcwritexml()
    
    #---默认不跑以下函数----
  #  modifycommandfe()
  #  modifycommandh5()
  #  modifycommandbe()
   # modifycommandbe()
    
    
    