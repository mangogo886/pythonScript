#!/usr/bin/env python

#coding:utf-8



import paramiko
import os
import sys



#sms6
def sms6Status():
        dirLists=['/data/CMPPGW_MAS_JP/','/data/CMPPGW_MAS_DD/','/data/CMPPGW_MAS_WX/','/data/CMPPGW_MAS_LJ/',
                  '/data/CMPPGW_MAS_SX/','/data/CMPPGW_MAS_MZ/','/data/CMPPGW_MAS_YD/','/data/CMPPGW_MAS_JY/','/data/CMPPGW_MAS_TY/','/data/CMPPGW_MAS_HH/',
                  '/data/CMPPGW_MAS_CF/','/data/CMPPGW_MAS_WP/','/data/CMPPGW_MAS_QZ/','/data/CMPPGW_MAS_SF/','/data/CMPPGW_MAS_SK/','/data/CMPPGW_MAS_JH/',
                  '/data/CMPPGW_MAS_XY/','/data/CMPPGW_MAS_XQD/','/data/CMPPGW_MAS_HY/','/data/CMPPGW_MAS_ZB/','/data/CMPPGW_MAS_WZ/']
        if len(sys.argv) < 2:
                print "The first number is phone,the second number is time...."

                sys.exit()
        else:
                phone=sys.argv[1]
                time=sys.argv[2]

                hostname='sms6'
                username='zjyw'
                ssh=paramiko.SSHClient()
                ssh.load_system_host_keys()
                privatekey=os.path.expanduser('/home/zjyw/.ssh/id_rsa')
                key=paramiko.RSAKey.from_private_key_file(privatekey)
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=hostname,username=username,pkey=key)
                prefix='smsstate.log'
                for dir in dirLists:
                        filePath="%s%s%s"%(dir,prefix,time)
                        listFile="ls %s"%(filePath)
                        stdin,stdout,stderr = ssh.exec_command(listFile)
                        if stdout.readline() !='':

                                cmdcat="cat %ssmsstate.log"%(dir)
                                grepcmd="|grep -a "
                                CMPPGW_MAS=cmdcat+str(time)+grepcmd+str(phone)
                                stdin,stdout,stderr=ssh.exec_command(CMPPGW_MAS)
                                CMPPGW_MASResults=stdout.readlines()
                                print "-------------------------------------sms6 search result--------------------------------------"
                                for CMPPGW in CMPPGW_MASResults:
                                        print "sms6 %s: "%(dir),CMPPGW
                        else:
                                print "%s not exist"%(filePath)
        ssh.close()



#sms7
def sms7Status():
        dirLists=['/data/CMPPGW_MAS_HY/','/data/CMPPGW_MAS_YD/','/data/CMPPGW_MAS_LC/','/data/CMPPGW_MAS_SW/','/data/CMPPGW_MAS_YD2/','/data/CMPPGW_MAS_XCT/',
                  '/data/CMPPGW_MAS_HUZ/','/data/CMPPGW_MAS_CH/','/data/CMPPGW_MAS_CW/','/data/CMPPGW_MAS_LS/','/data/CMPPGW_MAS_HY2/','/data/CMPPGW_MAS_TY/',
                  '/data/CMPPGW_MAS_ZY/','/data/CMPPGW_MAS_YF/','/data/CMPPGW_MAS_XDF/','/data/CMPPGW_MAS_YR/','/data/CMPPGW_MAS_LF/','/data/CMPPGW_MAS_HP/',
                  '/data/CMPPGW_MAS_JH2/','/data/CMPPGW_MAS_JX/','/data/CMPPGW_MAS_LK/','/data/CMPPGW_MAS_ZT/']
        if len(sys.argv) < 2:
                print "The first number is phone,the second number is time...."

                sys.exit()
        else:
                phone=sys.argv[1]
                time=sys.argv[2]

                hostname='sms7'
                username='zjyw'
                ssh=paramiko.SSHClient()
                ssh.load_system_host_keys()
                privatekey=os.path.expanduser('/home/zjyw/.ssh/id_rsa')
                key=paramiko.RSAKey.from_private_key_file(privatekey)
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=hostname,username=username,pkey=key)
                prefix='smsstate.log'
                for dir in dirLists:
                        filePath="%s%s%s"%(dir,prefix,time)
                        listFile="ls %s"%(filePath)
                        stdin,stdout,stderr = ssh.exec_command(listFile)
                        if stdout.readline() !='':

                                cmdcat="cat %ssmsstate.log"%(dir)
                                grepcmd="|grep -a "
                                CMPPGW_MAS=cmdcat+str(time)+grepcmd+str(phone)
                                stdin,stdout,stderr=ssh.exec_command(CMPPGW_MAS)
                                CMPPGW_MASResults=stdout.readlines()
                                print "-------------------------------------sms7 search result--------------------------------------"
                                for CMPPGW in CMPPGW_MASResults:
                                        print "sms7 %s: "%(dir),CMPPGW
                        else:
                                print "%s not exist"%(filePath)
        ssh.close()


if __name__=='__main__':
        sms6Status()
        sms7Status()