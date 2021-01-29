package main

import (
        "database/sql"
        "encoding/json"
        "fmt"
        _ "github.com/go-sql-driver/mysql"
        "github.com/toolkits/file"
        "io/ioutil"
        "log"
        "net/http"
        url2 "net/url"
        "os"
        "strings"
)

type Config struct {
        User     string `json:"user"`
        Password string `json:"password"`
        Address  string `json:"address"`
        School   string `json:"schoolName"`
}

func ParseConfig() (string, string, string, string) {
        //linux环境改这个方式
        filepath, _ := os.Getwd()
        filename := "config.json"
        //cfg := "E:\\golangworkspace\\src\\connmysql\\config1.json"
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

        return c.User, c.Password, c.Address, c.School
}

func runsql() {
        args := os.Args
        if args == nil || len(args) < 2 {
                log.Println("please entry exec dbname  and sqlfile...")
                return
        }
        dbname := args[1]
        filename := args[2]
        var DB *sql.DB
        u, p, url, app := ParseConfig()
        //linux环境改这个方式
        filepath, _ := os.Getwd()
        sqlfile := filepath + "/" + filename
        //sqlfile := "E:\\golangworkspace\\src\\connmysql\\" + filename
        f, err := os.Open(sqlfile)
        //file, err := ioutil.ReadFile(sqlfile)
        if err != nil {
                log.Println("找不到sql文件>>>>>", err)
                return
        }
        file, _ := ioutil.ReadAll(f)
        dblink := fmt.Sprintf("%s:%s@tcp(%s)/%s?charset=utf8", u, p, url, dbname)
        DB, err = sql.Open("mysql", dblink)
        if err != nil {
                log.Println("数据库连接失败.....")
                return
        }
        datalist := strings.Split(string(file), ";")

        for _, data := range datalist {
                data1 := strings.TrimSpace(data)
                if data1 != "" {
                        _, err := DB.Exec(data1)
                        if err != nil {
                                fmt.Printf("%s 出现报错>>>>>%s\n", data1, err)
                        }
                }
        }
        DB.Close()
        f.Close()
        //post数据到接口，生成一条数据库记录
        msg := map[string]string{"schoolname": app, "appCode": dbname, "sqlfile": filename}
        DataUrlVal := url2.Values{}
        for k, v := range msg {
                DataUrlVal.Add(k, v)
        }

        client := &http.Client{}
        req, _ := http.NewRequest("POST", "http://127.0.0.1:9999/version", strings.NewReader(DataUrlVal.Encode()))
        req.Header.Add("Content-Type", "application/x-www-form-urlencoded")
        resp, err := client.Do(req)
        if err != nil {
                fmt.Println("接口报错>>>", err)
        }
        resp.Body.Close()

}

func main() {
        runsql()
}