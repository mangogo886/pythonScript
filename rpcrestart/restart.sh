#!/bin/bash



cd /data/$name
P_ID=`ps -ef | grep -w "$name" | grep -w "$jar" | grep -v "grep" | awk '{print $2}'`


if [  -n "$P_ID" ];then
    kill -9 $P_ID
    echo "kill $P_ID"
fi

nohup /usr/local/jdk1.7.0_80/bin/java -Xms1024m -Xmx1024m  -jar $jar >>logs/nohup.out 2>&1 & echo "ok"