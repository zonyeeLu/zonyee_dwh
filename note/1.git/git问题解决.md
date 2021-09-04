## 1.git 无法打开问题
解决: 
- #### 打开如下网址获取 对应ip  

        a.github网址查询：https://link.zhihu.com/?target=https%3A//github.com.ipaddress.com/
        b.github域名查询：https://link.zhihu.com/?target=https%3A//fastly.net.ipaddress.com/github.global.ssl.fastly.net
        c.github静态资源ip：https://github.com.ipaddress.com
+ #### 将上述IP写到hosts中  

            a中ip 140.82.113.4 github.com
            b中ip 199.232.69.194 github.global.ssl.fastly.net
            c中ip 185.199.108.153 assets-cdn.github.com
            c中ip 185.199.109.153 assets-cdn.github.com
            c中ip 185.199.110.153 assets-cdn.github.com
            c中ip 185.199.111.153 assets-cdn.github.com
* #### cmd更新dns    
            cmd ipconfig /flushdns

