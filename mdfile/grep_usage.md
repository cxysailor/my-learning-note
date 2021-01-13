[toc]

# grep与正则表达式

## 1. grep简介

grep最重要的功能就是进行字符串数据的对比,然后将符合用户需求的字符串打印出来

grep用于分析一行信息,若当中有我们需要的信息,就将该行拿出来。可以解析一行文字,取得关键字,若该行有存在关键字,就会整行列出来

grep在数据中查寻一个字符串时,是以整行为单位来进行数据的选取。也就是说,假如一个文件内有10行,其中有2行具有你所查找的字符串,则将那2行显示在屏幕上,其它就丢弃

## 2. grep语法

```bash
grep [-aABcinv] [--color=auto] '查找字符' filename

选项与参数:

-a : 将二进制文件以文本文件的方式查找数据

-A : after,后面可以加数字n 除了输出该行外,后续的n行也列出来

-B : before,后面可以加数字n 除了输出该行外,前面的n行也列出来

-c : 计算找到'查找字符'的次数

-i : 忽略大小写

-n : 输出行时顺便将行号一起输出

-v : 反向选择,即显示出没有'查找字符'内容的行

--color=auto : 可以将找到的关键字部分加上颜色显示(Centos7默认已经加上了)
```
## 3. grep的基本用法

```bash
示例1 将last中,有root的那一行显示出来
❯ last | grep 'root'
root     pts/0        192.168.3.128    Mon Jan 11 12:10 - 14:04  (01:53)    
root     pts/0        192.168.3.128    Mon Jan 11 12:08 - 12:10  (00:02)    
root     pts/0        192.168.3.128    Mon Jan 11 12:05 - 12:08  (00:02)    
...以下省略...

示例2 将last中,选择没有root的那一行
❯ last | grep -v 'root'
cxy      pts/0        192.168.3.128    Tue Jan 12 16:44   still logged in   
reboot   system boot  3.10.0-1160.11.1 Tue Jan 12 16:42 - 17:34  (00:51)    
cxy      pts/1        192.168.3.128    Tue Jan 12 11:58 - 14:11  (02:13)
...以下省略...

示例3 在last输出的信息中,只要有root就取出,并且仅取第一栏
❯ last | grep 'root' | cut -d ' ' -f1
root
root
...以下省略...

示例4 取出/etc/man_db.conf内含MANPATH的那几行
❯ grep 'MANPATH' /etc/man_db.conf
# MANDATORY_MANPATH                     manpath_element
# MANPATH_MAP           path_element    manpath_element
# every automatically generated MANPATH includes these fields
#MANDATORY_MANPATH                      /usr/src/pvm3/man
MANDATORY_MANPATH                       /usr/man
...以下省略...

示例5 将关键字(RPC)所在行的前2行与后3行一起输出来
❯ dmesg | grep -A3 -B2 -n --color=auto 'RPC'
525-[   14.903096] device-mapper: uevent: version 1.0.3
526-[   14.903515] device-mapper: ioctl: 4.37.1-ioctl (2018-04-03) initialised: dm-devel@redhat.com
527:[   15.732569] RPC: Registered named UNIX socket transport module.
528:[   15.732574] RPC: Registered udp transport module.
529:[   15.732576] RPC: Registered tcp transport module.
530:[   15.732577] RPC: Registered tcp NFSv4.1 backchannel transport module.
531-[   15.816654] type=1305 audit(1610440985.931:4): audit_pid=526 old=0 auid=4294967295 ses=4294967295 subj=system_u:system_r:auditd_t:s0 res=1
532-[   23.108212] ip6_tables: (C) 2000-2006 Netfilter Core Team
533-[   23.277604] Ebtables v2.0 registered
第527-530行是我们要查找的RPC所在行,加上-A3与-B2选项后就将前2行与后3行一起输出了
```
## 4. grep的一些进阶用法 - 结合正则表达式

为演示这些用法,准备了一个文件regular_express.txt(在[鸟哥](http://linux.vbird_basic/0330regularex/regular_express.txt) 的网站上下载的)

```bash
❯ nl -ba regular_express.txt
1  "Open Source" is a good mechanism to develop programs.
2  apple is my favorite food.
3  Football game is not use feet only.
4  this dress doesn't fit me.
5  However, this dress is about $ 3183 dollars.
6  GNU is free air not free beer.
7  Her hair is very beauty.
8  I can't finish the test.
9  Oh! The soup taste good.
10  motorcycle is cheap than car.
11  This window is clear.
12  the symbol '*' is represented as start.
13  Oh!     My god!
14  The gd software is a library for drafting programs.
15  You are the best is mean you are the no. 1.
16  The world <Happy> is the same with "glad".
17  I like dog.
18  google is the best tools for search keyword.
19  goooooogle yes!
20  go! go! Let's go.
21  # I am VBird
22
```
这个文件共有22行,最后一行为空白行

```bash
例1 查找特定字符串

若要查找'the':

❯ grep -n 'the' regular_express.txt

8:I can't finish the test.
12:the symbol '*' is represented as start.
15:You are the best is mean you are the no. 1.
16:The world <Happy> is the same with "glad".
18:google is the best tools for search keyword.
------------------------------------------------
若要反向查找,即查找没有'the'这个字符串的行

❯ grep -vn 'the' regular_express.txt

1:"Open Source" is a good mechanism to develop programs.
2:apple is my favorite food.
3:Football game is not use feet only.
4:this dress doesn't fit me.
5:However, this dress is about $ 3183 dollars.
6:GNU is free air not free beer.
7:Her hair is very beauty.
9:Oh! The soup taste good.
10:motorcycle is cheap than car.
11:This window is clear.
13:Oh!  My god!
14:The gd software is a library for drafting programs.
17:I like dog.
19:goooooogle yes!
20:go! go! Let's go.
21:# I am VBird
22:
可以发现,除了8、12、15、16、18这5行之外的其它行都被列出来
------------------------------------------------
查找包含忽略大小写的'the'的行

❯ grep -in 'the' regular_express.txt

8:I can't finish the test.
9:Oh! The soup taste good.
12:the symbol '*' is represented as start.
14:The gd software is a library for drafting programs.
15:You are the best is mean you are the no. 1.
16:The world <Happy> is the same with "glad".
18:google is the best tools for search keyword.
------------------------------------------------
```
```bash
例2 利用中括号[]来查找集合字符

中括号里面不论有几个字符,它都仅代表某一个字符,即所有的字符之间是'或'的关系,匹配到任意一个即可

比如,想要在文件regular_express.txt中查找test和taste两个关键词

通过分析,这两个词有共同的't?st'部分存在,故可以这样这样查找

❯ grep -n 't[ae]st' regular_express.txt

8:I can't finish the test.
9:Oh! The soup taste good.
```

<++>
