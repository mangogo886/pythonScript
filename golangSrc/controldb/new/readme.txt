1.新版本，执行完sql之后，不管是否成功，都往接口地址: vs.qky100.cn/version(需配置host)，添加一条记录，
使用POST方法，传送三个字段：
schoolname（环境名称），appCode（执行的数据库），sqlfile(执行的sql文件),接口地址写死在代码
2.执行时，需要传入两个参数，第一是执行的数据库名称，第二是执行的sql文件名称