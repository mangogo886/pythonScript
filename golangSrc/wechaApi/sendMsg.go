package wechatscript


//企业微信脚本接口
import (
	"net/http"
	"fmt"
	"github.com/json-iterator/go"
	"io/ioutil"
	"bytes"
	"strings"
)


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
	fmt.Printf("成功获取到token: %s\n",json_str.Access_token)
	return json_str.Access_token
}

func send_Message(access_token,msg string){
	fmt.Print("开始发送消息\n")
	send_url:="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+access_token
	client:=&http.Client{}
	req,_:=http.NewRequest("POST",send_url,bytes.NewBuffer([]byte(msg)))
	req.Header.Set("Content-Type","application/json")
	resp,err:=client.Do(req)
	if err!=nil{
		fmt.Print(err)
	}
	fmt.Print(resp)
	defer resp.Body.Close()
}

func messages(touser string,toparty string,agentid int,content string) string {
	msg:=MESSAGES{
		Touser:touser,
		Toparty:toparty,
		Msgtype:"text",
		Safe:0,
		Agentid:agentid,
		Text: struct{ Content string `json:"content"`
		}{Content:content},
	}
	sed_msg,_:=json.Marshal(msg)
	return  string(sed_msg)
}

func main()  {
	touser:="zhumin"
	toparty:="2"
	agentid:=1
	corp_id:="wx8a57906aa7f1ae98"
	secret:="_iaWiNoeDHraPwm75V1v_bJEkN1ivFHgzFNoniKcSz8"
	accessToken:=getToken(corp_id,secret)
	content:="测试信息"
	msg:=strings.Replace(messages(touser,toparty,agentid,content),"\\\\","\\",-1)
	send_Message(accessToken,msg)
}
