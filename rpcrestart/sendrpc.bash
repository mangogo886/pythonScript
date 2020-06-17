#!/bin/bash

hostList=(app05 app11 app13)
rpclist=(qky-xjda-service qky-circle-service qky-msg-service qky-wechat-service)
localsh=/data/ops/script/restart.sh

commonDir=/data/
postfix1='-1.0-SNAPSHOT.jar'
postfix2='-0.0.1-SNAPSHOT.jar'



for host in ${hostList[@]}
do
for rpc in ${rpclist[@]}
do
if ssh $host test -f $commonDir$rpc/$rpc$postfix1
then
scp $localsh $host:$commonDir$rpc/logs 
ssh $host<<EOF
cd $commonDir$rpc/logs
sed -i  "/bash/a\name=$rpc"  restart.sh
sed -i  "/bash/a\jar=$rpc$postfix1"  restart.sh
chmod 755 restart.sh
exit
EOF
fi

if ssh $host test -f $commonDir$rpc/$rpc$postfix2
then
scp $localsh $host:$commonDir$rpc/logs 
ssh $host<<EOF
cd $commonDir$rpc/logs
sed -i  "/bash/a\name=$rpc"  restart.sh
sed -i  "/bash/a\jar=$rpc$postfix2"  restart.sh
chmod 755 restart.sh
exit
EOF
fi


done
done