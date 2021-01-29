package main

import (
        "database/sql"
        "encoding/json"
        "fmt"
        _ "github.com/go-sql-driver/mysql"
        "github.com/toolkits/file"
        "log"
        "net/http"
        "os"
)

type Config struct {
        User      string `json:"user"`
        Password  string `json:"password"`
        Address   string `json:"address"`
        Listening string `json:"listen"`
}

func ParseConfig() (string, string, string, string) {
        //linux环境改这个方式
        filepath, _ := os.Getwd()
        filename := "config.json"
        //cfg := "E:\\golangworkspace\\src\\connmysql\\recordconfig.json"
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
        return c.User, c.Password, c.Address, c.Listening
}

func getVerison(w http.ResponseWriter, r *http.Request) {
        database := "qky_ops"
        r.ParseForm()
        if r.Method == "POST" {
                u, p, link, _ := ParseConfig()
                dblink := fmt.Sprintf("%s:%s@tcp(%s)/%s?charset=utf8", u, p, link, database)
                DB, err := sql.Open("mysql", dblink)
                if err != nil {
                        log.Println(err)
                }
                stmt, _ := DB.Prepare("insert into qky_ops.record_version(school,appCode,sqlfile)values(?,?,?)")
                _, err = stmt.Exec(r.Form["schoolname"][0], r.Form["appCode"][0], r.Form["sqlfile"][0])
                if err != nil {
                        log.Println("insert报错>>>>>", err)
                        return
                }
                log.Println("成功插入记录表")
                stmt.Close()
        }
}

func main() {
        _, _, _, port := ParseConfig()
        http.HandleFunc("/version", getVerison)
        err := http.ListenAndServe(port, nil)
        if err != nil {
                log.Println(err)
        }
}