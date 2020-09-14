package main

import (
	"net"
	"fmt"
	"time"
	"os"
)

var ipaddress string="0.0.0.0:9998"


func process(conn net.Conn){
	defer conn.Close()
	//for直接开启一个死循环，接受客户端信息
	recemsg:=conn.RemoteAddr().String()
	fmt.Printf(" 客户端 %s 成功连接\n",recemsg)
	for{
		t:=time.Now()
		dates:=fmt.Sprintf("%d-%d-%d %d:%d:%d",t.Year(),t.Month(),t.Day(),t.Hour(),t.Minute(),t.Second())
		recemsg:=conn.RemoteAddr().String()
		clientip,_,_:=net.SplitHostPort(recemsg)
		file :="/root/ops/report-data/checkHost/result/"+clientip
		//创建一个新切片
		buf:=make([]byte,1024)
		_,err:=conn.Read(buf)
		if err!=nil{
			fmt.Printf("%s %s客户端断开连接.....\n",dates,conn.RemoteAddr(),err)
			return
		}
		//fmt.Print(string(buf[:n]))
		fmt.Printf("%s 接受客户端 的信息是:%s\n",dates,string(buf))
		_,err=os.Stat(file)
		if err!=nil{
			fmt.Printf("%s 不存在\n",file)
			os.Create(file)
			fmt.Printf("%s 创建文件\n",file)
		}

		f,err:=os.OpenFile(file,os.O_WRONLY,0755)
		if err!=nil{
			fmt.Printf("%s 文件不存在\n",file)
		}
		defer f.Close()
		_,err=f.WriteString(string(buf))
		fmt.Printf("%s 写入数据完成\n",dates)



	}
}

func main()  {
	t:=time.Now()
	dates:=fmt.Sprintf("%d-%d-%d %d:%d:%d",t.Year(),t.Month(),t.Day(),t.Hour(),t.Minute(),t.Second())
	listen,err:=net.Listen("tcp",ipaddress)
	if err!=nil{
		fmt.Println("Accept() err=",err )
		return
	}
	fmt.Printf("%s 服务端成功启动监听地址:%s\n",dates,ipaddress)
	defer listen.Close()
	for{
		conn,err:=listen.Accept()
		if err!=nil{
			fmt.Println("Accept() err=",err)
		}
		/*关键字go就是协程(goroutine)的关键字，
		使用go调用一个函数或者方法，就可以实现并发
		 */
		go process(conn)
	}

}