package main

import (
	"net"
	"fmt"
	"encoding/json"
	"time"
	"github.com/toolkits/nux"
	"github.com/toolkits/core"
	"io/ioutil"
	"os/exec"
)
var serverip="172.16.6.5:9998"
//var serverip="0.0.0.0:9998"


func check()map[string]interface{}  {

	result:=make(map[string]interface{})

	//ip
	ipaddress:=exec.Command("/bin/bash","-c",`ip addr | awk '/^[0-9]+: / {}; /inet.*global/ {print gensub(/(.*)\/(.*)/, "\\1", "g", $2)}'|head -1`)
	stdout,err:=ipaddress.StdoutPipe()
	if err!=nil{
		fmt.Printf("%s\n",err)
	}
	ipaddress.Start()
	ipResult,err:=ioutil.ReadAll(stdout)
	if err!=nil{
		fmt.Printf("%s\n",err)
	}
	result["ip"]=string(ipResult)



	//cpu 5分钟负载
	cpu,_:=nux.LoadAvg()
	avg5min:=cpu.Avg5min
	fmt.Printf("cpu 5分钟负载:%-10.2f\n",avg5min)
	result["cpuload5"]=avg5min
	//内存
	mem, err := nux.MemInfo()
	if err!=nil{
		fmt.Println(err,"\n")
	}
	memFree := mem.MemFree + mem.Buffers + mem.Cached
	memUsed := mem.MemTotal - memFree
	var t uint64 = 1024 * 1024*1024
	result["memTota"]=mem.MemTotal/t
	result["memUse"]=memUsed/t

	//磁盘
	mountPoints, err := nux.ListMountPoint()
	if err!=nil{
		fmt.Println(err,"\n")
	}
	var ret [][]interface{} = make([][]interface{}, 0)
	for idx := range mountPoints {
		var du *nux.DeviceUsage
		du, err = nux.BuildDeviceUsage(mountPoints[idx][0], mountPoints[idx][1], mountPoints[idx][2])
		if err == nil {
			ret = append(ret,
				[]interface{}{
					du.FsSpec,
					core.ReadableSize(float64(du.BlocksAll)),
					core.ReadableSize(float64(du.BlocksUsed)),
					core.ReadableSize(float64(du.BlocksFree)),
					fmt.Sprintf("%.1f%%", du.BlocksUsedPercent),
					du.FsFile,
					core.ReadableSize(float64(du.InodesAll)),
					core.ReadableSize(float64(du.InodesUsed)),
					core.ReadableSize(float64(du.InodesFree)),
					fmt.Sprintf("%.1f%%", du.InodesUsedPercent),
					du.FsVfstype,
				})
		}

	}

	result["dfInfo"]=ret
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
		time.Sleep(time.Duration(3600)*time.Second)
		t:=time.Now()
		dates:=fmt.Sprintf("%d-%d-%d %d:%d:%d",t.Year(),t.Month(),t.Day(),t.Hour(),t.Minute(),t.Second())
		sendmsg, _ := json.Marshal(check())
		fmt.Printf("%s 执行查询结果\n",dates)
		_, err = conn.Write([]byte(sendmsg))

		if err != nil {
			fmt.Printf("%s %s 服务端断开，客户端自动退出", dates, conn.RemoteAddr())
			return
		}

	}



}