package main

import (
        "time"
        "fmt"
        "net/http"
        "log"
        "github.com/toolkits/nux"
        "github.com/toolkits/core"
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
        //内存
        mem, _ := nux.MemInfo()
        memFree := mem.MemFree + mem.Buffers + mem.Cached
        var t uint64 = 1024 * 1024*1024
        fmt.Fprint(w,"cpu 负载:",cpudata,"\n","磁盘:",ret,"\n","内存(GB):",memFree/t,mem.MemTotal/t,"\n")
}