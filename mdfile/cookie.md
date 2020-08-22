# Cookie简介

## 1. 问题缘由

由于http/https协议是无状态的，即服务器不会记录每次请求的状态。这样就使得一些需要登录的网站，在登录后

使用requests发起第二次请求时，不能获取预期的结果，而是请求到登录的页面。

这是因为服务器端不知道第二次请求是基于登录状态下的请求，故而没有获取到需要的信息。

而使用浏览器时却可以记录登录状态。这就使用到了一种叫做cookie的东西。

## 2. Cookie

Cookie是用来让服务器端记录客户端的相关状态的。

### 2.1 Cookie的来源

通过浏览器的抓包工具，对登录页面进行抓包分析。在输入帐号、密码等信息后，点击登录，在抓包工具中找到有关login的数据包，

在Response Headersz中有set-cookie.

由此可见，cookie是在发起第一次post请求时，由服务器端生成的。

```
cache-control: no-cache
content-length: 43
content-type: image/gif
date: Sat, 22 Aug 2020 08:24:44 GMT
expires: Thu, 01 Jan 1970 00:00:01 GMT
p3p: CP="NOI DSP COR CURa ADMa DEVa PSAa PSDa OUR IND UNI PUR NAV"
pragma: no-cache
server: nginx
set-cookie: tbsa=1fda91d5d8729bf73c1b4e88_1598084684_3; path=/; domain=.mmstat.com; SameSite=none; Secure
set-cookie: atpsida=95a9fb0b152eeed6f8ec9731_1598084684_3; path=/; domain=.mmstat.com; SameSite=none; Secure
status: 200
```
使用浏览器继续访问该网站的其他页面时，就会自动携带这个cookie。这样服务器端就知道了是已经登录状态，就可以

访问到需要的内容。

### 2.2 Cookie的使用

基于上面的介绍，在使用requests发起请求时，也携带上这个cookie就可以实现与浏览器访问一样的效果了，从而

也可以获取我们预期的内容。

使用Cookie有2中方式

#### 2.2.1 手动处理

使用浏览器的抓包工具，找到cookie，将其复制，然后添加的代码的headers中，在发起Requests请求时，设置headers参数

```python
headers ={
		'cookie': 'cna=U1zCF+U97iYCASeAEzDmZAKn; sca=5a5a0212; tbsa=1fda91d5d8729bf73c1b4e88_1598084654_2; atpsida=95a9fb0b152eeed6f8ec9731_1598084654_2; atpsidas=26452b9ec21671f76c187d22_1598084654_2; cad=1741544c10c-5750485462922608630001; cap=4be3',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
requests.post(url=url, headers=headers)
```
但是不建议这样使用cookie，原因一个因为比较麻烦；另一个是cookie有时效，过一段时间就会失效，甚至有些网站的cookie是动态的。

#### 2.2.2 自动处理

这里需要用到session会话对象，有2个作用：
- 可以进行请求的发送
- 如果请求过程中产生了cookie，则该cookie会被自动存储/携带在该session对象中

基于此，可以这样自动处理cookie：
- 创建一个session对象 `session = requests.Session()` 
- 使用session对象进行模拟登录post请求的发送 - cookie会被存储中该session中
- session对象对其它页面对应的get请求进行发送 - 携带了cookie

```python
# 创建session对象
session = requests.Session()
# 使用session发送post请求 - 存储了cookie
response = session.post(url=url, headers=headers, data=data)
# 接下来，使用携带了cookie的session发送get请求
page_text = session.get(url=page_url, headers=headers).text
```


