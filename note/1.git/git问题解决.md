## 1.git 无法打开问题
**解决:** 
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

## 2.git无法push代码
**提示内容**
-         remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
          remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for
          more information 
-         不再支持通过密码的方式提交代码，需要通过personal token才行
**解决:**
+ 生成token
+        github->settings->developer settings->personal access tokens
         **注意保存token,因为只会显示一次**
+ 仓库增加token 或者 重新clone
+     git remote set-url origin https://<your_token>@github.com/<USERNAME>/<REPO>.git
      git clone https://<your_token>@github.com/<USERNAME>/<REPO>.git