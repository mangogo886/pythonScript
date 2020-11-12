package main

import (
        "time"
        "fmt"
        "net/http"
        "log"
        "github.com/toolkits/nux"
        "github.com/toolkits/core"
        "os"
)

func main()  {
        t:=time.Now()
        dates:=fmt.Sprintf("%d-%d-%d %d:%d:%d",t.Year(),t.Month(),t.Day(),t.Hour(),t.Minute(),t.Second())
        fmt.Printf("%s 接口进程启动成功\n",dates)

        http.HandleFunc("/report",systeminfo)
        err:=http.ListenAndServe(":1999",nil) //启动一个htpp端口，handler参数一般设置为nil
        if err!=nil{
                log.Fatal(err)
        }


}



func systeminfo(w http.ResponseWriter,r *http.Request){
        //定义日志文件输出
        str,_:=os.Getwd()
        filepath:=str+"/"+"out.log"
        f,err:=os.OpenFile(filepath,os.O_WRONLY|os.O_CREATE|os.O_APPEND,0644)
        if err!=nil{
                log.Fatal(err)
        }
        defer  f.Close()
        logger:=log.New(f,"\r\n", log.Ldate | log.Ltime | log.Lshortfile)
        //log.SetOutput(f)
        logger.SetOutput(f)



        //cpu
        cpudata, _ := nux.LoadAvg()
        mountPoints, _ := nux.ListMountPoint()
        //磁盘
        var ret [][]interface{} = make([][]interface{}, 0)
        for idx := range mountPoints {
                var du *nux.DeviceUsage
                du, err := nux.BuildDeviceUsage(mountPoints[idx][0], mountPoints[idx][1], mountPoints[idx][2])
                if err == nil {
                        ret = append(ret,
                                []interface{}{
                                        //du.FsSpec,
                                        fmt.Sprintf("挂载目录: %s,",du.FsSpec),
                                        //core.ReadableSize(float64(du.BlocksAll)),
                                        fmt.Sprintf("磁盘总量: %s,",core.ReadableSize(float64(du.BlocksAll))),
                                        //core.ReadableSize(float64(du.BlocksUsed)),
                                        fmt.Sprintf("已用空间: %s,",core.ReadableSize(float64(du.BlocksUsed))),
                                        //core.ReadableSize(float64(du.BlocksFree)),
                                        fmt.Sprintf("剩余空间: %s,",core.ReadableSize(float64(du.BlocksFree))),
                                        //fmt.Sprintf("%.1f%%", du.BlocksUsedPercent),
                                        //du.FsFile,
                                        //core.ReadableSize(float64(du.InodesAll)),
                                        //core.ReadableSize(float64(du.InodesUsed)),
                                        //core.ReadableSize(float64(du.InodesFree)),
                                        //fmt.Sprintf("%.1f%%", du.InodesUsedPercent),
                                        //du.FsVfstype,
                                })
                }
        }
        //内存
        mem, _ := nux.MemInfo()
        memFree := mem.MemFree + mem.Buffers + mem.Cached
        var t uint64 = 1024 * 1024*1024
        //fmt.Fprintln(w,"cpu 负载:",cpudata,"\n","磁盘:",ret,"\n","内存(GB):",memFree/t,mem.MemTotal/t,"\n")
        fmt.Fprintln(w,"cpu 负载:",cpudata)
        fmt.Fprintln(w,"磁盘:",ret)
        fmt.Fprintln(w,"内存(GB):","剩余内存: ",memFree/t,"总内存: ",mem.MemTotal/t)
        /*
        log.Println("cpu 负载:",cpudata)
        log.Println("磁盘:",ret)
        log.Println("内存(GB):","剩余内存: ",memFree/t,"总内存: ",mem.MemTotal/t)
        */
        logger.Println("cpu 负载:",cpudata)
        logger.Println("磁盘:",ret)
        logger.Println("内存(GB):","剩余内存: ",memFree/t,"总内存: ",mem.MemTotal/t)
}