package main

import (
	"net"
	"fmt"
	"encoding/json"
	"time"
	"io/ioutil"
	"os/exec"
)
var serverip="172.16.6.5:9998"




func check()map[string]string  {
	result:=make(map[string]string)

	ipaddress:=exec.Command("/bin/bash","-c",`ip addr | awk '/^[0-9]+: / {}; /inet.*global/ {print gensub(/(.*)\/(.*)/, "\\1", "g", $2)}'`)
	stdout,err:=ipaddress.StdoutPipe()
	if err!=nil{
		fmt.Printf("%s\n",err)
	}
	ipaddress.Start()
	ipResult,err:=ioutil.ReadAll(stdout)
	if err!=nil{
		fmt.Printf("%s\n",err)
	}


	result["IP"]=string(ipResult)

	dfTotal:=exec.Command("/bin/bash","-c",`df -Ph|grep VolGroup-lv_root|awk '{print $2}'`)
	stdout,err=dfTotal.StdoutPipe()
	if err!=nil{
		fmt.Printf("%s\n",err)
	}
	dfTotal.Start()
	totalResult,err:=ioutil.ReadAll(stdout)
	if err!=nil{
		fmt.Printf("%s\n",err)
	}
	result["dfTotal"]=string(totalResult)


	dfuse:=exec.Command("/bin/bash","-c",`df -Ph|grep VolGroup-lv_root|awk '{print $3}'`)
	stdout,err=dfuse.StdoutPipe()
	if err!=nil{
		fmt.Printf("%s\n",err)
	}
	dfuse.Start()
	dfusresult,err:=ioutil.ReadAll(stdout)
	if err!=nil{
		fmt.Printf("%s\n",err)
	}

	result["dfUse"]=string(dfusresult)


	memTotal:=exec.Command("/bin/bash","-c",`free -g|grep Mem|awk '{print $2}'`)
	stdout,err=memTotal.StdoutPipe()
	if err!=nil{
		fmt.Printf("%s\n",err)
	}
	memTotal.Start()
	memTotalreslut,err:=ioutil.ReadAll(stdout)
	if err!=nil{
		fmt.Printf("%s\n",err)
	}

	result["memTotal"]=string(memTotalreslut)

	memUse:=exec.Command("/bin/bash","-c",`free -g|grep Mem|awk '{print $3}'`)
	stdout,err=memUse.StdoutPipe()
	if err!=nil{
		fmt.Printf("%s\n",err)
	}
	memUse.Start()
	memUsereslut,err:=ioutil.ReadAll(stdout)
	if err!=nil{
		fmt.Printf("%s\n",err)
	}

	result["memUse"]=string(memUsereslut)


	cpuload:=exec.Command("/bin/bash","-c",`cat /proc/loadavg|awk '{print $3}'`)
	stdout,err=cpuload.StdoutPipe()
	if err!=nil{
		fmt.Printf("%s\n",err)
	}
	cpuload.Start()
	cpuloadreslut,err:=ioutil.ReadAll(stdout)
	if err!=nil{
		fmt.Printf("%s\n",err)
	}
	result["load5"]=string(cpuloadreslut)

	return result
}



func main() {
	t:=time.Now()
	dates:=fmt.Sprintf("%d-%d-%d %d:%d:%d",t.Year(),t.Month(),t.Day(),t.Hour(),t.Minute(),t.Second())
	conn, err := net.Dial("tcp", serverip)
	if err != nil {
		fmt.Printf("%s %s 服务端无法连接，请检查服务端是否正常启动", dates, serverip)
		return
	}
	fmt.Printf("%s 成功连接到服务端：%s",dates,conn.RemoteAddr())

	for{
		t:=time.Now()
		dates:=fmt.Sprintf("%d-%d-%d %d:%d:%d",t.Year(),t.Month(),t.Day(),t.Hour(),t.Minute(),t.Second())
		time.Sleep(time.Duration(3600)*time.Second)
		sendmsg, _ := json.Marshal(check())
		fmt.Printf("%s 执行查询结果\n",dates)
		_, err = conn.Write([]byte(sendmsg))

		if err != nil {
			fmt.Printf("%s %s 服务端断开，客户端自动退出", dates, conn.RemoteAddr())
			return
		}

	}



}