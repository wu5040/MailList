#!/bin/zsh
##添加用户，并且在/home/ 下为用户生成用户目录。
cat < users.txt | xargs -n 1 useradd -m
##批处理模式下更新密码
chpasswd < userpwd.txt
##将上述的密码转换到密码文件和组文件
pwconv
##结束验证信息
echo "OK 新建完成"
