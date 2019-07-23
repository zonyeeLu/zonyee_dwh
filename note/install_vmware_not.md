1.安装完虚拟机之后root密码忘记 解决方案  
(1)用当前用户 sudo passwd  
(2)输入当前用户的密码  
(3)设置新的root密码  

2.查看linux系统版本信息  
cat /proc/version  

3.ubuntu 关闭防火墙  
(1) 查看防火墙状态  sudo ufw status  
(2) inactive状态是防火墙关闭状态(sudo ufw disable) active是开启状态(sudo ufw enable)

4.出现错误:  
Unable to lock the administration directory (/var/lib/dpkg/), is another process using it?  
原因:  
新安装完系统后，首次登陆系统，使用 apt update 发现一直更新不了。每次都提示这个错误。看了下错误提示，是因为系统锁被别的进程占用了（每次新装完 Ubuntu 系统时，内部会缺少比较多的软件源，这时候系统会自动启动更新进程 apt-get  
解决方案:  
等工具升级完成 或者 退出更新  

5.ubuntu 安装 ssh :   
(1) apt-get install openssh-server  
(2) /etc/init.d/ssh start  
    启动成功会提示： 
[ ok ] Starting ssh (via systemctl): ssh.service.  并且 /etc/init.d/ 路径下会有ssh
(3) 检查是否成功 ps -e|grep ssh    
(4) 重启虚拟机就可以了

6.ubuntu 安装mysql   
(1) 查看是否安装了mysql  netstat -tap | grep mysql   
(2) sudo apt-get install mysql-server mysql-client  -- 输入root 密码  
(3) 查看是否安装成功  sudo netstat -tap | grep mysql  
