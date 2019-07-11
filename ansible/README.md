# ansibleOps
ansible运维  
这个文件/roles/zkhosts/tasks/main.yml，主要使用了ansible 的lineinfile模块。用来在指定文件添加内容  

相关参数:  
dest: /etc/hosts   --要操作的目标文件  
regexp: '^127.0.0.1' ---匹配的内容，用了正则表达式，一般需要修改或者删除，就用regexp参数去匹配相关内容  
insertbefore: '^# The following'  ---参数insertbefore，把要添加的内容加在这个参数值的前面  
insertafter： '^# The following'  ---参数 insertafter，把要添加的内容加在这个参数值的后面  
line: '195.18.20.22 mc.zk.thinkjoy.cn'  ---参数line的值。是要添加的内容  
