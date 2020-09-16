package main

//企业微信http接口
import (
	"net/http"
	"log"
	"github.com/json-iterator/go"
	"io/ioutil"
	"fmt"
	"bytes"
	"strings"
	"time"
)

var toparty="2"
var agentid=1
var corp_id="wx8a57906aa7f1ae98"
var secret="_iaWiNoeDHraPwm75V1v_bJEkN1ivFHgzFNoniKcSz8"
var json = jsoniter.ConfigCompatibleWithStandardLibrary

type JSON struct {
	Access_token string `json:"access_token"`
}

type MESSAGES struct {
	Touser string `json:"touser"`
	Toparty string `json:"toparty"`
	Msgtype string `json:"msgtype"`
	Agentid int `json:"agentid"`
	Text struct {
		//Subject string `json:"subject"`
		Content string `json:"content"`
	} `json:"text"`
	Safe int `json:"safe"`
}

var json_str JSON


func getToken(corp_id string,secret string) string{
	var json_str JSON
	tokenUrl:="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid="+corp_id+"&corpsecret="+secret
	client:=&http.Client{}
	req,err:=client.Get(tokenUrl)
	defer  req.Body.Close()
	body,_:=ioutil.ReadAll(req.Body)
	if err!=nil{
		fmt.Printf("无法访问微信企业url:%s\n",tokenUrl)
	}

	json.Unmarshal([]byte(body),&json_str)
	//fmt.Printf("成功获取到token: %s\n",json_str.Access_token)
	return json_str.Access_token
}

func send_Message(w http.ResponseWriter,r *http.Request){
	accessToken:=getToken(corp_id,secret)
	send_url:="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+accessToken

	if r.Method=="POST"{
		t:=time.Now()
		dates:=fmt.Sprintf("%d-%d-%d %d:%d:%d",t.Year(),t.Month(),t.Day(),t.Hour(),t.Minute(),t.Second())
		_=r.ParseForm()
		fmt.Printf("%s 信息接收人:%s\n",dates,r.Form["tos"][0])
		fmt.Printf("%s 发送的信息是:%s\n",dates,r.Form["content"][0])
		msg:=MESSAGES{
			Touser:r.Form["tos"][0],
			Toparty:toparty,
			Msgtype:"text",
			Safe:0,
			Agentid:agentid,
			Text: struct{ Content string `json:"content"`
			}{Content:r.Form["content"][0]},
		}
		sed_msg_tmp,_:=json.Marshal(msg)
		sed_msg:=string(sed_msg_tmp)
		messges:=strings.Replace(sed_msg,"\\\\","\\",-1)
		client:=&http.Client{}
		req,_:=http.NewRequest("POST",send_url,bytes.NewBuffer([]byte(messges)))
		req.Header.Set("Content-Type","application/json")
		resp,err:=client.Do(req)
		if err!=nil{
			fmt.Print(err,"\n")
		}
		//fmt.Print(resp,"\n")
		fmt.Printf("%s 信息发送完成\n",dates)
		defer resp.Body.Close()
	}
}



func main()  {
	t:=time.Now()
	dates:=fmt.Sprintf("%d-%d-%d %d:%d:%d",t.Year(),t.Month(),t.Day(),t.Hour(),t.Minute(),t.Second())
	fmt.Printf("%s 接口进程启动成功\n",dates)

	http.HandleFunc("/wechatapi",send_Message)
	err:=http.ListenAndServe(":9090",nil) //启动一个htpp端口，handler参数一般设置为nil

	if err!=nil{
		log.Fatal(err)
	}

}