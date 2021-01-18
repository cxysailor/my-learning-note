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

**例1 查找特定字符串** 

```bash
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
**例2 利用中括号[]来查找集合字符**

```bash
中括号里面不论有几个字符,它都仅代表某一个字符,即所有的字符之间是'或'的关系,匹配到任意一个即可

比如,想要在文件regular_express.txt中查找test和taste两个关键词

通过分析,这两个词有共同的't?st'部分存在,故可以这样这样查找

❯ grep -n 't[ae]st' regular_express.txt

8:I can't finish the test.
9:Oh! The soup taste good.

查找有oo的字符
❯ grep -n 'oo' regular_express.txt

1:"Open Source" is a good mechanism to develop programs.
2:apple is my favorite food.
3:Football game is not use feet only.
9:Oh! The soup taste good.^M
18:google is the best tools for search keyword.
19:goooooogle yes!

查找有oo的字符,但是不想要前面带有g的
❯ grep -n '[^g]oo' regular_express.txt

2:apple is my favorite food.
3:Football game is not use feet only.
18:google is the best tools for search keyword. # 这一行是因为有tools符合条件
19:goooooogle yes! # 这一行是因为o比较多,会有ooo、oooo...这样的组合,故也符合条件

oo前面不想有小写字母
❯ grep -n '[^a-z]oo' regular_express.txt 或
❯ grep -n '[^[:lower:]]oo' regular_express.txt

3:Football game is not use feet only.
注:若一组集合字符中,该字符组是连续的,比如大写英文字母、小写英文字母、数字等,就可以使用[a-z]、[A-Z]、[0-9]方式书写;若是要求字符串是英文字母与数字时,就把它们写在一起[a-zA-Z0-9]这样了

获取有数字的行
❯ grep -n '[0-9]' regular_express.txt 或
❯ grep -n '[[:digit:]]' regular_express.txt

5:However, this dress is about $ 3183 dollars.
15:You are the best is mean you are the no. 1.
```
英文与数字选取的特殊字符

| 特殊符号   | 代表意义                                         |
| ------     | ------                                           |
| [:alnum:]  | 英文大小写字符及数字,即0-9 a-z A-Z               |
| [:alpha:]  | 任何英文大小写字符,即a-z A-Z                     |
| [:blank:]  | 空格键与[Tab]键两者                              |
| [:cntrl:]  | 键盘上的 控制按键 包括CR、LF、Tab、Del等         |
| [:digit:]  | 数字,即0-9                                       |
| [:graph:]  | 除了空格符(空格键与Tab)外的其它所有按键          |
| [:lower:]  | 小写字符,即a-z                                   |
| [:print:]  | 任何可以被打印出来的字符                         |
| [:punct:]  | 标点符号(punctuation symbol),即"'?!;:#$          |
| [:upper:]  | 大写字符,即A-Z                                   |
| [:space:]  | 任何会产生空白的字符,包括空格键、[Tab]、CR等     |
| [:xdigit:] | 十六进制的数字类型,包括0-9、A-F、a-f的数字与字符 |

**例3 行首字符^与行尾字符$** 

```bash
查找行首为the的行
❯ grep -n '^the' regular_express.txt

12:the symbol '*' is represented as start.

查找开头是小写字符的行
❯ grep -n '^[a-z]' regular_express.txt 或
❯ grep -n '^[[:lower:]]' regular_express.txt

2:apple is my favorite food.
4:this dress doesn't fit me.
10:motorcycle is cheap than car.
12:the symbol '*' is represented as start.
18:google is the best tools for search keyword.
19:goooooogle yes!
20:go! go! Let's go.

查找不是以英文字母开头的行
❯ grep -n '^[^a-zA-Z]' regular_express.txt 或
❯ grep -n '^[^[:alpha:]]' regular_express.txt

1:"Open Source" is a good mechanism to develop programs.
21:# I am VBird
```
*这个^符号在中括号[]内外的区别* 

- 在中括号内 - [^xxx] - 表示反向选择,即不包含xxx的行
- 在中括号外 - \^[xxx] - 表示以xxx开头,即定位在行首的意思

```bash
查找行尾是点(.)的行 # 小数点有特殊意义,故需要使用转义字符\转义为普通的字符小数点
❯ grep -n '\.$' regular_express.txt

1:"Open Source" is a good mechanism to develop programs.
2:apple is my favorite food.
3:Football game is not use feet only.
4:this dress doesn't fit me.
10:motorcycle is cheap than car.
11:This window is clear.
12:the symbol '*' is represented as start.
15:You are the best is mean you are the no. 1.
16:The world <Happy> is the same with "glad".
17:I like dog.
18:google is the best tools for search keyword.
20:go! go! Let's go.
```
文件regular_express.txt中第5-9行也是以小数点结尾的,为什么没有输出来?

我们先把第5-10行打印出来看看到底有什么区别

```bash
❯ cat -nA regular_express.txt | head -n 10 | tail -n 6

     5  However, this dress is about $ 3183 dollars.^M$  # Windows的换行符
     6  GNU is free air not free beer.^M$
     7  Her hair is very beauty.^M$
     8  I can't finish the test.^M$
     9  Oh! The soup taste good.^M$
    10  motorcycle is cheap than car.$  # Linux的正常换行符
```
可以看到,第5-9行的结尾是以[\^M\$]作为换行符,而正常的Linux的应该是[\$]结尾的;所以第5-9行没有被选择出来

```bash
查找空白行 - 就是没有输入任何数据的行
❯ grep -n '^$' regular_express.txt

22:
```
```bash

很多文件中会有多行空白行与开头为#的注释行,为节省输出空间,可以将这些空白行与注释行去掉
❯ grep -v '^$' /etc/rsyslog.conf | grep -v '^#'

$ModLoad imuxsock # provides support for local system logging (e.g. via logger command)
$ModLoad imjournal # provides access to the systemd journal
$WorkDirectory /var/lib/rsyslog
$ActionFileDefaultTemplate RSYSLOG_TraditionalFileFormat
$IncludeConfig /etc/rsyslog.d/*.conf
$OmitLocalLogging on
$IMJournalStateFile imjournal.state
*.info;mail.none;authpriv.none;cron.none                /var/log/messages
authpriv.*                                              /var/log/secure
mail.*                                                  -/var/log/maillog
cron.*                                                  /var/log/cron
*.emerg                                                 :omusrmsg:*
uucp,news.crit                                          /var/log/spooler
local7.*                                                /var/log/boot.log
```
**例4 任意一个字符.(小数点)与重复字符\*(星号)** 

- . (小数点) : 代表[一定有一个任意字符]
- \* (星号)  : 代表[重复前一个字符,0到无穷多次],为组合形态

```bash
找出g??d这样的字符串,即包括4个字符,以g开头d结尾,中间包含2个字符
❯ grep -n 'g..d' regular_express.txt

1:"Open Source" is a good mechanism to develop programs.
9:Oh! The soup taste good.
16:The world <Happy> is the same with "glad".

因为中间一定存在两个字符,所以使用小数点
```
```bash
获取类似o、oo、ooo、oooo这样的字符串

想当然的,应该是o*这样子的吧?试试看
❯ grep -n 'o*' regular_express.txt

1:"Open Source" is a good mechanism to develop programs.
2:apple is my favorite food.
3:Football game is not use feet only.
4:this dress doesn't fit me.
5:However, this dress is about $ 3183 dollars.
6:GNU is free air not free beer.
7:Her hair is very beauty.
8:I can't finish the test.
9:Oh! The soup taste good.
10:motorcycle is cheap than car.
11:This window is clear.
12:the symbol '*' is represented as start.
13:Oh!  My god!
14:The gd software is a library for drafting programs.
15:You are the best is mean you are the no. 1.
16:The world <Happy> is the same with "glad".
17:I like dog.
18:google is the best tools for search keyword.
19:goooooogle yes!
20:go! go! Let's go.
21:# I am VBird
22:

怎么会全部输出了呢(带o的不带o的都选择了)？

原来星号*代表的是重复前面字符0个或多个的意思,所以o*代表的就是[有空字符或一个o以上的字符],才选择了所有行出来

应该是oo*这样子才对
❯ grep -n 'oo*' regular_express.txt

1:"Open Source" is a good mechanism to develop programs.
2:apple is my favorite food.
3:Football game is not use feet only.
4:this dress doesn't fit me.
5:However, this dress is about $ 3183 dollars.
6:GNU is free air not free beer.
9:Oh! The soup taste good.
10:motorcycle is cheap than car.
11:This window is clear.
12:the symbol '*' is represented as start.
13:Oh!  My god!
14:The gd software is a library for drafting programs.
15:You are the best is mean you are the no. 1.
16:The world <Happy> is the same with "glad".
17:I like dog.
18:google is the best tools for search keyword.
19:goooooogle yes!
20:go! go! Let's go.

```

<++>
