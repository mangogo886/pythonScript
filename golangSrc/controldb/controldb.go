package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"github.com/toolkits/file"
	"io/ioutil"
	"log"
	"os"
	"strings"
)

type Config struct {
	User     string `json:"user"`
	Password string `json:"password"`
	Address  string `json:"address"`
}

func ParseConfig() (string, string, string) {
	//linux环境改这个方式
	//filepath, _ := os.Getwd()
	//filename := "config.json"
	cfg := "E:\\golangworkspace\\src\\connmysql\\config.json"
	//cfg := filepath + "/" + filename

	if !file.IsExist(cfg) {
		log.Println(cfg, "is not existent")
	}
	var c Config
	configContent, err := file.ToTrimString(cfg)
	err = json.Unmarshal([]byte(configContent), &c)

	if err != nil {
		log.Println("parse config file:", cfg, "fail:", err)
	}

	return c.User, c.Password, c.Address
}

func runsql() {
	args := os.Args
	if args == nil || len(args) < 2 {
		log.Println("please entry exec dbname and sqlfile...")
		return
	}
	dbname := args[1]
	filename:=args[2]
	var DB *sql.DB
	u, p, url := ParseConfig()
	//linux环境改这个方式
	//filepath, _ := os.Getwd()
	//sqlfile := filepath+"/"+filename
	sqlfile := "E:\\golangworkspace\\src\\connmysql\\"+filename
	file, err := ioutil.ReadFile(sqlfile)
	if err != nil {
		log.Println("找不到sql文件>>>>>",err)

	}

	dblink := fmt.Sprintf("%s:%s@tcp(%s)/%s?charset=utf8", u, p, url, dbname)
	DB, err = sql.Open("mysql", dblink)
	if err != nil {
		log.Println("数据库连接失败.....")
	}
	datalist := strings.Split(string(file), ";")

	for _, data := range datalist {
		_, err := DB.Exec(data)
		if err != nil {
			log.Println("执行错误的sql>>>>>>", err)
		}
		log.Println("执行成功的sql>>>>>", data)

	}

}

func main() {
	runsql()
}
