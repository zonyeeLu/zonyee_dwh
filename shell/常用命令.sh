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
free -h  # 查看内存 --human 可读的

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

# 13.并行执行 &
#!/bin/bahs 
for i in 1 2 3 4 5
do{
    echo $i
}&
done

# 14. 定时器 crontab -e
# 0-59 分
# 0-23 时
# 1-31 日
# 1-12 月
# 0-7  周(0或者7都是周日)
crontab -e 30 17 * * 6 sh home/tmp/test.sh # 每周六17:30执行一次 test.sh 脚本

# 15.变量
# 双引号"",允许使用$引用其他变量
# 单引号'',禁止引用其他变量,$视为普通字符
# 反撇``,将命令执行的结果输出给变量

# 16. 测试文件
[ -d home/zonyee24 ] # 判断tmp是为目录 0为是, 非0为否
[ -f home/zonyee24 ] # 判断tmp是为文件 0为是, 非0为否
# -r 当前用户是否可读  -w 当前用户是否可写 -x 当前用户是否有执行权限 -e 判断目录或者文件是否存在
echo $?  # 返回上一条命令的结果 
# 例子
if [ -f /home/zonyee24/test.sh ]
then 
    echo "test.sh is exists"
else 
    echo "test.sh is not exists"
    touch test.sh # 不存在则创建一个
fi

# 17. $用法
$0  #返回脚本名字
$1  #1-9返回脚本入参
$?  #返回上一条命令的状态 0为是, 非0为否
$#  #返回脚本参数个数

# 18. 整数值比较
[ 10 -eq 20]  # 比较10跟20的数值大小 -ne 不等 -gt 大于 -lt 小于 -le小于或等于  -ge 大于或等于

# 19. find 
find ./ -name "*.sh" # 找出当前目录下sh的文件
find ./ -user root # 找出当前目录下属主为root的文件
find ./ -perm 777 # 找出当前目录下权限为777的文件
find ./ -type -d # 找出当前目录下为目录的文件夹
find ./ -name "*.sh" | xargs ls -l 
nohup find / -name "*.sh" > info.log 2>&1 & # 找出根目录下所有sh文件,并且日志输出到info.log  nohup表示后台输出
#! /bin/bash
for ((i=0; i<10; i++))
do 
  touch $1$i.sh 
done

# 20. tail 
tail -f info.log  # 监控日志增长

# 21. grep 查找
grep -i "test" info.log  #找出test所在的行 
grep -n "test" info.log  #找出test所在的行  以及行号
grep -c "test" info.log  #找出test所在的行数

# 22. sed 编辑
sed -n '1,2'd info.log  # 删除第一第二行
sed in '2'p info.log  # print第二行

# 21. awk 根据内容进行分析
awk '{print $1}' info.log  # 默认按照空格分隔,输出每一行的第一列
awk -F: '{print $1}' info.log  # 按照冒号,输出每一行的第一列