package main

import (
	"database/sql"
	"encoding/json"
	_ "github.com/go-sql-driver/mysql"
	"github.com/samuel/go-zookeeper/zk"
	"github.com/toolkits/file"
	"log"
	"net"
	"os"
	"strings"
	"time"
)

type Config struct {
	Zkaddress string `json:"zkaddress"`
	Databases string `json:"databases"`
	Listen    string `json:"listen"`
}

func ParseConfig() (string, string, string) {
	//linux环境改这个方式
	filepath, _ := os.Getwd()
	filename := "config.json"
	//cfg:="E:\\golangworkspace\\src\\connectzk\\config.json"
	cfg := filepath + "/" + filename

	if !file.IsExist(cfg) {
		log.Println(cfg, "is not existent")
	}
	var c Config
	configContent, err := file.ToTrimString(cfg)
	err = json.Unmarshal([]byte(configContent), &c)
	if err != nil {
		log.Println("parse config file:", cfg, "fail:", err)
	}

	return c.Zkaddress, c.Databases, c.Listen
}

func syszk() {
	var flags int32 = 0
	var acls = zk.WorldACL(zk.PermAll)
	var DB *sql.DB
	zkhost, dburl, _ := ParseConfig()
	zkconn, _, err := zk.Connect([]string{zkhost}, time.Second*5)
	if err != nil {
		log.Println(err)
	}

	DB, _ = sql.Open("mysql", dburl)
	if err := DB.Ping(); err != nil {
		log.Println("数据库连接失败")
	}
	row, err := DB.Query("select appCode,path,content,mark from zk_node;")
	if err != nil {
		log.Println(err)
	}

	for row.Next() {
		var appCode string
		var path string
		var content string
		var mark int

		var tempnode string

		_ = row.Scan(&appCode, &path, &content, &mark)
		//把路径分割成数组
		splitNode := strings.Split(path, "/")
		if mark == 0 {

			//遍历每个分割的数组
			for _, node := range splitNode {
				//拼接路径，递归创建节点
				tempnode += "/" + node
				nodepath := "/" + strings.TrimLeft(tempnode, "/")
				nodebool, _, _ := zkconn.Exists(nodepath)
				if !nodebool {
					//zkconn.Set(nodepath, nil, flags)
					zkconn.Create(nodepath, nil, flags, acls)
				}
			}
			//nodebool1,_,_:=zkconn.Exists(path)
			//修改节点值，需要先获取节点状态，再通过Version去修改，否则无法修改
			_, state, _ := zkconn.Get(path)
			zkconn.Set(path, []byte(content), state.Version)
			_, _ = DB.Exec("update zk_node set mark=1 where mark=? and path=?", 0, path)
			log.Println(path, "成功同步到zookeeper..........", content)
			//
		}
	}
	zkconn.Close()
	DB.Close()
}

func main() {
	_, _, ip := ParseConfig()
	listen, err := net.Listen("tcp", ip)
	if err != nil {
		log.Println(err)
	}
	log.Println("监听地址:", ip)
	log.Println("read config file: cfg successfully")
	defer listen.Close()
	for {
		time.Sleep(time.Second * 15)
		syszk()
	}
}
