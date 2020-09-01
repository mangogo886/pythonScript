#!/usr/bin/env python
#coding:utf8
#批量修改jk job主机

import os
import glob
import xml.etree.ElementTree as ET
import ConfigParser




def readxml():
    for dirpath in frontendpath:
        filepath=dirpath+configfile
        if os.path.exists(filepath):
            tree = ET.parse(filepath)
            root = tree.getroot()
            host=root.find('buildWrappers').find('jenkins.plugins.publish__over__ssh.BapSshPostBuildWrapper').find('postBuild').find('delegate').find('publishers').find('jenkins.plugins.publish__over__ssh.BapSshPublisher').find('configName').text
            command=root.find('buildWrappers').find('jenkins.plugins.publish__over__ssh.BapSshPostBuildWrapper').find('postBuild').find('delegate').find('publishers').find('jenkins.plugins.publish__over__ssh.BapSshPublisher').find('transfers').find('jenkins.plugins.publish__over__ssh.BapSshTransfer').find('execCommand').text
            print "部署应用-----",dirpath
            print "部署主机-----",host
            print "部署命令-----",command

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
            print "修改前端job ",filepath,"部署主机为 ",fehost
            #print "部署应用-----",dirpath
            #print "部署主机-----",root.find('buildWrappers').find('jenkins.plugins.publish__over__ssh.BapSshPostBuildWrapper').find('postBuild').find('delegate').find('publishers').find('jenkins.plugins.publish__over__ssh.BapSshPublisher').find('configName').text
            #print "部署命令-----",command


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
            print "修改前端job ",filepath,"部署主机为 ",fehost
            #print "部署应用-----",dirpath
            #print "部署主机-----",root.find('buildWrappers').find('jenkins.plugins.publish__over__ssh.BapSshPostBuildWrapper').find('postBuild').find('delegate').find('publishers').find('jenkins.plugins.publish__over__ssh.BapSshPublisher').find('configName').text
            #print "部署命令-----",command



#后端和rpc
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
                tree.write(jobspathbe)
                print "修改jobs文件 ",jobspathbe,"部署主机为 ",host

            else:
                print jobspathbe,"job文件不存在"

            #拼接service config.xml，并判断
            jobspathrpc=commondir+ap+rpcsuffix+"/"+configfile
            if os.path.exists(jobspathrpc):
                hostname=root.find('buildWrappers').find('jenkins.plugins.publish__over__ssh.BapSshPostBuildWrapper').find('postBuild').find('delegate').find('publishers').find('jenkins.plugins.publish__over__ssh.BapSshPublisher').find('configName')
                hostname.text=host
                tree.write(jobspathrpc)
                print "修改jobs文件 ",jobspathrpc,"部署主机为 ",host
            else:
                print jobspathrpc,"job文件不存在"




if __name__=="__main__":
    frontendpath=glob.glob("/data/.jenkins/jobs/qky-*-frontend/")
    h5path=glob.glob("/data/.jenkins/jobs/qky-*-h5/")
    commondir="/data/.jenkins/jobs/"
    bksuffix="-backend"
    rpcsuffix="-service"
    configfile="config.xml"
    configPath="config.ini"
    fehost="ng01"

   # readxml()
    fewritexml()
    bewritexml()
    h5writexml()