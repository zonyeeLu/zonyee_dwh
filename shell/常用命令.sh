#!/bin/bash 

# 1. 查看历史命令 history 
history    # 用户输入的历史所有命令
history 10 #用户数据最近是个命令
!10        # 执行用户历史第十个命令

# 2. 设置命令别名 alias 存放位置 ~/.bashrc
alias                 # 查看自定义命令别名
alias d='df -Th'      # 输入d相当于输入 df -Th 
unalias d             # 解除d的命令

# 3. 查看磁盘大小
df -Th 

# 4. 用户根目录
~

# 5. help命令
df --help 

# 6. 打印当前工作目录  print word directory
pwd

# 7. 输出重定向 >覆盖  >>追加
ls > ./tmp/test.txt     # 将ls的输出结果覆盖到test.txt中 >默认为1>
ls >> ./tmp/test.txt    # 将ls的输出结果追加到test.txt中 >>默认为1>>
cdc 2> ./tmp/test.txt   # 将命令执行的错误信息覆盖到test.txt 中
cdc 2>> ./tmp/test.txt  # 将命令执行的错误信息追加到test.txt 中 

#! /bin/bash
# test.sh 
ls -l 
pwdd 

bash test.sh 
bash test.sh 2> ./tmp/test.txt     # 将错误的信息都往test.txt覆盖写入
bash test.sh > ./tmp/test.txt      # 将正确的信息都往test.txt覆盖写入
bash test.sh &> ./tmp/test.txt     # 将正确和错误的信息都往test.txt覆盖写入
bash test.sh >> ./tmp/test.txt 2>&1  # 将正确和错误的信息都往test.txt中追加写入 2> 通过1的管道写入


# 8. 查看内存
free -h  # 查看内容 --human 可读的

# 9. 查找
grep -i mem  # 输出包含mem的行 ,忽略大小写 

# 10. 管道操作符 |
free -h|grep -i mem  # 在free -h中查找包含mem的行 -i忽略大小写
free -h|grep -i mem|awk '{print $4}'  # 在free -h中查找包含mem的行 -i忽略大小写 并且输出第四列  print $0输出整行

# 11. 文件权限
  # d rwx d表示为目录directory  r表示read  w表示write x表示执行

# 12. 用户权限
  # 用户分为 所有者(u) 所属组(g) 其他用户(o)
#   例子 -rw-r--r-- 1 root root  0 xxx   shell.txt 
#   1. 文件所有者 root 创建者为root 
#   2. 文件所有者(root用户)对shell.txt 有 rw权限
#   3. 文件所属组(root组内其他用用户)对shell.txt 有r权限
#   4. 其他用户(root组以外其他用用户)对shell.txt 有r权限

# 12. 文件权限 chmod
chmod 777 ./tmp/test.txt # 给test.txt所有用户授rwx的所有权限
chmod a+x ./tmp/test.txt # 等价上一条命令
chmod a-x ./tmp/test.txt # 给test.txt删除可执行权限
chmod g-x,o-x ./tmp/test.txt # 组内用户删除可执行 其他用户删除可执行权限
