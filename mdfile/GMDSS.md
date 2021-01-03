[toc]
# GMDSS评估题目 - 设备实操题目

## Part 1. IMARSAT-C

### Inmarsat-C 题卡1

#### 1. 查看船位信息，并报告目前MES同步的卫星

首页右下角处看船位；屏幕下方中部NCS:IOR LOGIN

#### 2. 在《Admiralty List of Radio Signals》Vol5中查找新加坡RCC的电传号码，存入地址簿中

- NP285,先在书后面查询索引，找到Singapore的SAR在第400页，查到RCC的电传号码:+87 20021
- F8(Setup)-9(Configuration)-Station List 找到一个空白，按enter
- 输入以下信息：
    - Station Group:可以不填
    - Station Name:Singapore RCC
    - Country Code:87
    - Station ID:20021
    - 其它的信息保持默认

#### 3. 泰安海轮呼号TAHS拟从澳大利亚的悉尼港到青岛港，按报文标准格式编辑并保存抵港报告。电文的主要内容：向COSCOTJ报告本船拟在5天后到达青岛港

- F1(File)-New 打开的窗口中输入以下内容
```bash
TO:COSCOTJ
FM:MV TAIANHAI/TAHS
DD:14/NOV/2020

SUBJECT:ETA TO QINGDAO

WE WILL ARRIVE YOUR GOOD PORT QINGDAO IN 5 DAYS.

B.RGDS
MASTER OF MV TAIANHAI

```
- 编辑完成后，再次F1(File)-4 Save
- 打开的窗口中输入一个文件名比如：etaqingdao，完成保存

#### 4. 如何利用C站进行快速遇险报警

- 直接按DISTRESS键4秒中

### Inmarsat-C 题卡2

#### 1. 解释MES主菜单OPTIONS的子菜单各项实现的功能

- Options的子菜单及其功能
    - 1. Login 入网
    - 2. Logout 出网
    - 3. Abort 放弃
    - 4. Select NCS 选择NCS
    - 5. Ocean Region 选择洋区
    - 6. LES Information 地面站的信息
    - 7. Test 测试

#### 2. 本船位于卫星覆盖的重叠区，转换洋区，洋区同步入网后报告NCS的编码。

- Options - 5 Ocean Region-Pacific
- 首页上Current NCS：244

#### 3. 将指定的已存电文，经北京地面站发往上海外带，用户邮箱为:market@penavico.sh.cn

- 编辑并保存电文
- 保存地址
- 发送电文
```bash
F3(Transmit)
- Priorty:Normal
- Message File:选择编辑好的电文
- Station Name:选择保存的地址
- Destination Type:E-mail
- LES ID:211(Beijing Marine)
- 光标移动到[TRANSMIT]
- Enter发送
```
#### 4. 设置每天12:00向公司自动报告本船位置信息(公司联系方式:Telex-08532237;Fax-861065293421)

- 保存地址
- Reports - Message Report - Message Report 1

### Inmarsat-C 题卡3

#### 1. 查看MES近期的收发信息记录

Logs

#### 2. PSC对C站检查内容的准备工作有哪些？

- 检查电源的状况
- 检查天线
- C站各个部分的连接
- PV测试及其记录
- 人员培训及其记录
- 操作程序的张贴
- 检查的记录

#### 3. C站快速报警后，确定险情可控，不需要外界援助，用C站完成后续的遇险信息解除的通信

- 编辑并保存电文
    - F1(File)-New
    - F1(File)-Close 根据提示保存
- 发送电文
    - F3(Transmit)-Transmit Message

#### 4. *在《Admiralty List of Radio Signals》Vol5中查找从中国青岛港到澳大利亚东航线经过的航行警告区域，并说明澳大利亚采用何种方式播发MSI*

- NP285中P322 X8 X7,P260 SafetyNet
- 澳大利亚使用SafetyNet播发MSI,不再使用NAVTEX

### Inmarsat-C 题卡4

#### 1. 解释MES主菜单各项的功能

#### 2. C站设有保安报警，与遇险报警有何区别？

#### 3. 鞍山货轮(ASCN)正航行与印度孟买附近，将指定电文通过附近LES发送传真到中远非洲公司，给定用户fax:27-11-61666561

#### 4. 从《Admiralty List of Radio Signals》Vol5查找上述海域的SafetyNet播发的N/W和W/X的时间，并设置EGC接收信息

### Inmarsat-C 题卡5

#### 1. 如何在文件管理中完成电文的删除操作

- File - 5 Delete

#### 2. 查看本机的IMN码

- Setup - 2 System Setup - IMN
- 或首页主屏幕右上角IMN

#### 3. 育强轮(BOXZ)在马来西亚的马六甲海峡附近搁浅，编辑遇险优先等级电文通过新加坡LES发送到RCC报告本船所处的位置、当前的时间等较为详尽的情况，希望得到拖轮救助(注：遇险发射确认时仅为口述)

- 编辑电文并保存
    - File - New
        - MAYDAY MAYDAY MAYDAY
        - THIS IS MV YUQIANG YUQIANG YUQIANG
        - MAYDAY YUQIANG BOXZ
        - I AN AGROUND AT MALAKA STRAIT CLOSE TO MALYSIA IN POSITION 0102N/10234E AT 1230UTC ON 27/NOV/2019
        - REQUIRE A TUG ASSISTANCE
    - File - close or Save - 输入文件名maydaymsg保存文件
- Transmit - Transmit Message 根据提示发送电文

#### 4. 如何防止C站误报警

- 所有操作人员经过培训并持有相应的证书
- 指定熟悉设备操作的专门人员负责
- 张贴操作说明
- 张贴防止误报警的提醒
- 应急按钮装在不容易触碰的地方
- 张贴误报警的取消操作程序
- 对人员定期进行操作培训
- 对设备进行良好的维护和保养

### Inmarsat-C 题卡6

#### 1. 查看离当前时间最近一次的EGC信息，并说明接收EGC信息的类型

- F4(EGC) - 1 Display

#### 2. 完成C站机内时钟的校对，并显示UTC时间

- Setup - 2 System Setup

#### 3. 远河轮(YHCN)的EPIRB设备在新加坡开航前进行设备测试时误发了报警信息。利用C站编辑误报警取消电文，并发送该误报警的取消信息

- 首先关闭EPIRB，停止误报警的继续发射
- 编辑取消误报警的电文，说明在什么时间什么位置因为什么原因误发的遇险报警，然后发送给新加坡RCC取消该误报警

#### 4. C站关机时需要注意什么问题

- 先退网(Logout),否则C站可能一直在入网(Lonin)状态，可能会继续产生费用
- 然后再关机

### Inmarsat-C 题卡7

#### 1. 说明C站当前的工作状态。如果工作状态设置为EGC接收状态，电文能否正常收发?

- 首页主屏幕左下角显示:Current State:Idle(当前状态:空闲)
- EGC设备分类及其特点
    - 0类 标准EGC接收机
    - 1类 标准C站,不能接收EGC信息
    - 2类 标准C站+EGC接收机,不能同时工作
        - 第1种 合用模式(Inm-C) - 接收CES电文时不能接收EGC信息,空闲时间接收EGC
        - 第2种 EGC接收模式(EGC only) - 只能接收EGC信息,不能收发常规C站报文,但是可以发送遇险信息
    - 3类 标准C站+EGC接收机,且能同时工作

#### 2. 根据评估员的要求，从地址簿中删除指定的通信地址

- F8 Setup - 打开地址簿 - 删除要求的Station Name

#### 3. 育强轮(BOXZ)航行于日本海域时，船员突发疾病需要岸上急救。通过医疗救助业务完成通信操作。

- Transmit发送编辑好的求助电文
- 在发射选择页面中
    - Destination Type:**SPEC** 
    - Station ID:**38** 
    - 其它选项正常

#### 4. 从《Admiralty List of Radio Signals》Vol5查找澳大利亚东南海域的SafetyNet播发N/W和W/X的时间，并设置EGC接收信息

- NP285 Page 246

### Inmarsat-C 题卡8

#### 1. 机内GPS出现故障，手动输入当前船位信息为3630S/13030E

- F9 Position

#### 2. 按需求将EGC信息只做存盘处理，并关闭C站自动打印的设置

- Setup - 6 Auto Mode Setup

#### 3. 船舶发生进水险情，向RCC发送含遇险性质的遇险报警(注:遇险发射仅为口述)

- Setup - 1 Distress Alert Setup
- Nature:Flooding
- 按Distress按钮

#### 4. 完成设备PV/Link Test

- Options - 7 Test - PV Test

## Part 2 MF/HF DSC

### MF/HF DSC 题卡1

#### 1. 在《Admiralty List of Radio Signals》Vol1中查出上海海岸电台MMSI及DSC值守频率

- NP281(2) Page118/Page126

#### 2. 船舶在抵达青岛港前，通过上海岸台进行HF DSC呼叫测试

- 按下2DSC键 - TEST CALL - 编妥 - 按CALL键

### MF/HF DSC 题卡2

#### 1. 调看最近接收到的DSC遇险级别电文

- 按下6SCAN键
- 再按下0LOG键

#### 2. 编发MF遇险呼叫:遇险船育强(BOXZ),船位N3614/E06525,时间06:25UTC,遇险性质失控,后续通信方式:无线电话。指出随后遇险通信使用频率

- 直接按DISTRESS键或按2DSC键,打开DSC编辑菜单
- 编辑以下信息
    - CallType: Distress
    - Nature: Disable
    - Position: N3614/E06525
    - Time: 06:25UTC
    - Com: Radiotelephone
    - DSC Freq: 2187.5kHz/4207.5kHz
- 按下Distress键4秒

### MF/HF DSC 题卡3

#### 1. 将本船船位更新为3605N/12023E

- 6SCAN - Setup - Position

#### 2. 育强轮(BOXZ)有船员落水，请周围船只注意暸望，后续通信方式为无线电话通信频率为2182kHz。编发紧急呼叫，并在MF DSC遇险安全频率上发射

- Distress - Man Over Board

### MF/HF DSC 题卡4

#### 1. 进行DSC自测试，报告测试结果

- 按下3TEST键，显示如下信息
    - PLL - 锁相环
    - RF - 射频
    - PA1 - 放大器
    - COMB - 滤波器
    - TxFIL - 发射滤波器
    - COUPL - 耦合器

#### 2. 编辑所有台呼叫，优先等级为安全，后续通信方式为FEC电传，频率为2174.5kHz，在MF DSC遇险和安全频率上发出呼叫

- 2DSC - All Ships

### MF/HF DSC 题卡5

#### 1. 进行DSC自测试，报告测试结果

- 同题卡4第1题

#### 2. 船-船MF DSC呼叫，预约在2200.0kHz上进行常规无线电话通信

- 按下2DSC键，打开DSC编辑菜单
- 编辑如下内容
    - CallType: Individual
    - Station ID: ship's MMSI
    - Priority: Routine
    - Com.Type: Telephone
    - Com.Freq: 2200.0kHz/2200.0kHz
    - DSC Freq: 合适的频率
- 按下CALL键4秒

### MF/HF DSC 题卡6

#### 1. 在《Admiralty List of Radio Signals》Vol1中查出广州海岸电台MMSI及DSC值守频率

- NP281(2) Page121/Page117

#### 2. 在2187.5kHz快速遇险报警，指出随后遇险通信的方式和频率

- 直接按DISTRESS键4秒中
- 报警发出后默认的随后通信方式为电话，通信频率为2182kHz

### MF/HF DSC 题卡7

#### 1. 外接GPS出现故障，手动输入当前船位信息为3630N/13030E

- 按下6SCAN键
- Setup
- Position - 直接输入船位

#### 2. 如果在2187.5kHz发生DSC误报警，如何取消

- 关机，停止发射，再开机
- 在2182kHz频率上使用无线电话广播取消报警的信息
- 如果有可能，报告相应的RCC取消报警信息

### MF/HF DSC 题卡8

#### 1. 查看DSC遇险值守频率

- 按下6SCAN键，即显示当前值守的所有遇险频率

#### 2. 在8414.5kHz快速遇险报警，指出随后的通信方式和频率

- 发射快速遇险报警
	* 按下Distress键
	* DSC Freq: 8414.5kHz
	* 按下Distress键4秒
- 查看随后通信方式和频率
    - Telephone
    - 8291.0kHz

## Part 3. VHF

### VHF 题卡1

#### 1. 解释VHF控制面板数字字母键的第二功能

- 1 - 静音
- 2 - 亮度调节
- 3TEST - 测试
- 4IntCom - 内部通信用
- 5ACK - 确认(手动/自动)
- 6PRINT - 打印
- 7INTL/USA - 模式切换；对记忆频道扫描
- 8SCAN -扫描所有频道
- 9DW - 双值守(16频道和另外一个频道同时值守)
- 0HI/LO - 高/低功率转换

#### 2. 调节静噪

- 调节SQUELCH旋钮，到噪声刚刚消失

#### 3. 远盛湖轮欲用VHF设备联系银河轮，约定在CH13上通电话，说明可行方法，并完成整个通信过程

- 第1种方法
  - 发送一个DSC呼叫序列通知银河轮在Ch13上通话
      - 按下CALL/MSG
      - 选择Ship Call
      - 输入银河轮的MMSI
      - 指定随后的通信方式为VHF电话和通信频道为Ch13
      - 按下CALL/MSG键3秒发出
      - 机器自动转到Ch13，进行通话
- 第2种方法
    - 使用VHF在Ch16上呼叫银河
    - 叫通后，双方约定转到Ch13上通话
    - 手动转到Ch13，进行通话

- 以上两种方法，通话完毕后记得转换回Ch16值守

### VHF 题卡2

#### 1. 选择Ch13并设置为低功率发射

- 转换到Ch13
- 按下SHIFT,再按下0HI/LO键
- 看到面板上显示LO字样

#### 2. 设置Ch12与Ch16双值守

- 转换到Ch12
- 按下SHIFT，再按9DW键
- 屏幕会交替显示Ch12和Ch16

#### 3. 育强轮(BOXZ)在A2海区(位置5814N/15025E)失控漂流，利用VHF设备编发遇险报警

- 按下CALL/MSG
- 选择Distress
- 输入船位
- 遇险性质:Disable and Drift
- 按CALL/MSG键3秒发出

### VHF 题卡3

#### 1. 更新本船船位和当前时间，并说明更新原则

- MENU - Position - Mannual
- 当内置GPS出现故障时，需要更新船位

#### 2. 完成设备自测试，并解释测试结果

- 按下3TEST键，显示如下信息
    - TX POWER    : OK 发射功率
    - TX/RX PCB   : OK 发射/接收电路
    - CPU PCB     : OK cpu电路
    - CH70 RX PCB : OK 70频道接收电路
    - DUP RX PCB  : OK 双工接收电路

#### 3. 同题卡2第3题

### VHF 题卡4

#### 1. 查看本台VHF DSC自识别码和群呼码

- MENU - System - Self ID / Group ID list

#### 2. 将DSC收妥方式设置为手动

- 按下SHIFT键
- 再按5ACK
- 屏幕上显示Manual Ack

#### 3. 育强轮(BOXZ)在黄海海域(A1海区)遇险，情况紧急，快速发射DSC遇险报警

- 直接按下Distress键4秒

### VHF 题卡5

#### 1. 查看上海海岸电台的MMSI和VHF无线电话业务

- NP281(2) Page126

#### 2. 育强轮在长江口锚地，扫描接收上海海岸电台的VHF电话信道

- 这个设置记忆频道扫描的操作
- 查NP281(2) Page118,获得上海海岸电台值守频道为Ch16、Ch20、Ch21、Ch26、Ch27
- 将这5个频道存储为记忆频道(Ch16可以不存，因为该频道默认必须扫描值守)
    - MENU
    - Memery Channel
    - 分别存入上述频道
- 按下SHIFT键，再按7INTL/USA键，切换到MEMO模式
- 按下SHIFT键，再按8SCAN键开始扫描这些频道

#### 3. 同题卡2第3题

### VHF 题卡6

#### 1. 打开/关闭扬声器，调节音量

- Shift + 1键 打开/关闭扬声器
- 调节Volume/Power旋钮 调节音量

#### 2. 调节控制面板亮度和对比度

- Shift + 2键 调节亮度
- Shift + Channel旋钮 调节对比度

#### 3. 育强轮(BOXZ)于13:25UTC在A1海区不慎发射VHF DSC误报警，如何取消?并说明如何防止误报警

- 取消误报警的操作
    - 关掉机器电源，停止继续发射
    - VHF Ch16广播取消误报警的信息
        - 船名
        - 呼号
        - 误报警的时间(UTC)
        - 取消该误报警
    - 继续守听Ch16
    - 联系相应的岸台，取消该误报警
- 防止误报警的发生
    - 操作人员经过培训，并获取相应的证书
    - 禁止无关人员操作、接触设备
    - 张贴操作说明
    - 张贴防止误报警的说明
    - 演习时对设备进行操练

### VHF 题卡7

#### 1. 取消DSC低优先等级报警信号的音频报警

- MENU - Alarm - Ext Alarm - Routine - Off

#### 2. 查看DSC发射、接收记录

- 按下LOG键，即可看到收发记录

#### 3. 说明VHF设备日常管理和维护的内容，并解释VHF波段重要信道(Ch16、Ch70、Ch06、Ch13)的作用

- 日常管理和维护内容
    - 定期检查电源电压输出是否正常
    - 定期检查天线(2根)是否固定，连接是否正常
    - 定期自测试
    - 定期发射测试
        - 对岸呼叫
        - DSC测试
        - 本船2台设备间测试
    - 在VHF无线电话使用登记簿上进行通信登记并签署
- 各个信道的作用
    - Ch16 - VHF频段无线电话遇险与安全信道
    - Ch70 - VHF DSC遇险呼叫、紧急呼叫、安全呼叫和常规呼叫信道
    - Ch06 - 用于船舶电台与从事协调搜救的航空器之间的信道；还用于冰封季节航空器电台、破冰船和救助船间信道
    - Ch13 - 船舶航行安全通信信道，主要用于船舶间的航行安全通信；还可用于船舶移动和港口作业;发布气象信息

## Part 4. EPIRB

### EPIRB题卡1

#### 1. 从支架上取下EPIRB，做完第2题后再安装回原来位置

#### 2. 找出EPIRB设备上的船名、呼号标识并指出电池和静水压力释放器的有效期

### EPIRB题卡2

#### 1. 说明人工和自动启动EPIRB的方法

- 人工启动
    - 将保护盖左移，ON键按一下
- 自动启动
    - 扔进海里即可自动启动

#### 2. 完成EPIRB自测试

- 按下TEST按钮10秒，白灯闪3下，松开

### EPIRB题卡3

#### 1. 说明EPIRB控制开关在各个位置的作用

#### 2. 完成EPIRB自测试

### EPIRB题卡4

#### 1. 说明人工和自动启动EPIRB的方法

#### 2. 完成EPIRB自测试

## Part 5. SART

### SART 题卡1

#### 1. 指出标志在SART上的船名、呼号

#### 2. 对SART进行测试

### SART 题卡2

#### 1. 在船上如何开启并正确安装SART

- 拔掉销子，转到ON位置
- 绑在驾驶台两侧比较开阔处

#### 2. 对SART进行测试

### SART 题卡3

#### 1. 在救生艇上如何开启并正确安装SART

- 开启后安装在救生艇外面最高处

#### 2. 指出标志在SART上电池的有效期

### SART 题卡4

#### 1. 指出标志在SART上的船名、呼号和电池有效期

#### 2. 对SART进行测试

## Part 6. Inmarsat-F

### Inmarsat-F 题卡1

#### 1. 在手柄话机终端查看船站所跟踪的卫星

- 开机进入工作状态后，屏幕初始显示的卫星为EOR

#### 2. 设置北京地面站为常规通信缺省(Default)地面站

- Menu - Super User(密码:12345678) - LES Config - Default LES - 根据跟踪的卫星选择 - 北京(Beijing)

#### 3. 给青岛某用户拨打电话，号码为85752167

- 拿起话机直接拨号:00 86 532 8575 2167#(即:00 + 电话国家码 + 城市码 + 电话号码),接通后即可通话，通话完毕挂机

### Inmarsat-F 题卡2

#### 1. 设置新加坡地面站为遇险报警缺省地面站

- Menu - Super User - LES Config - Distress LES - 根据跟踪的卫星选择 - 新加坡(Sigapore)

#### 2. 查看本船船位

- Menu - Status - GPS Info - PositionInfo

#### 3. 新加坡船海河(9VGH3)(Inm-F:763127808)航行于印度洋，欲与该船进行电话通信，说明通信过程

- 直接拨号00 870 763127808(即00 + 洋区码 + 船台电话号码)#,接通后即可通话，通话完毕挂机

### Inmarsat-F 题卡3

#### 1. 解释手柄话机主要按键的功能(数字按键除外)

#### 2. 查看移动站的通信记录

- Menu - Super User - Call Logs - Logged Calls

#### 3. 本移动站在检验过程中，不慎通过北京地面站发送误报警，请予以取消(育强BOXZ,Inm-F763125676),并说明如何防止F站误报警

- 取消该误报警
    - 查阅无线电信号表，找到北京RCC的电话10 6529 2221
    - 拨打北京RCC的电话，接通后说明如下信息，取消误报警
        - 船名      : 育强
        - 呼号      : BOXZ
        - F站识别码 : 763125676
        - 时间      : 1230UTC on 19/Mar/2012
        - 说明信息  : 我船在上述时间使用F站发射了误报警，请取消
- 防止误报警的发生
    - 按钮放在不容易触碰的地方
    - 所有操作人员经过培训并持有相应的证书
    - 操作人员熟悉设备的操作
    - 张贴注意事项
    - 张贴误报警的取消方式和程序

### Inmarsat-F 题卡4

#### 1. 检查移动站的工作状态是否正常

- 查看初始状态即可判断

#### 2. 查看船站故障报警记录

#### 3. 育强BOXZ，位置N3604/E12020失火，要求立即援助；遇险时间为1400UTC，发送遇险报警

- 按下Distress键5秒,接通电话后将需要的信息告知对方

### Inmarsat-F 题卡5

#### 1. 查看本船船位信息

- 同题卡2第2题

#### 2. 校对F船站日期时间

- Menu - Super User - Set UTC Time

#### 3. 同题卡4第3题

### Inmarsat-F 题卡6

#### 1. 给定一份传真件，将该传真件发给青岛用户85752555

- 打开传真机电源
- 放入要发送的传真件
- 拨号00 86 532 85752555#
- 点击发送

#### 2. 如何进行遇险报警的后续通信，并说明遇险通信应报告哪些主要信息

- 查无线电信号表，找到RCC的电话，比如00 86 10 65292221
- 拨号00861065292221#
- 接通后，报告如下内容
    - 船名
    - 呼号
    - 遇险时间
    - 遇险地点
    - 遇险性质
    - 所需要的援助

### Inmarsat-F 题卡7

#### 1. 由《Admiralty List of Radio Signals》Vol5中查出中国搜救协调中心电话号码，并存入地址簿中

- 查NP285 - 找到中国RCC电话 - 00861065292221 - 2nd+C +输入电话00861065292221

#### 2. 根据保存的中国搜救协调中心电话，取消本船Inmarsat-C发射的误报警，并说明如何防止F站误报警。(给定本船信息:育强BOXZ，C站号码441219018,误报警时间0735UTC)

- 取消误报警的操作
	* 查NP285 - 中国RCC电话
	* 拨号00861065292221#
	* 接通后，报告如下内容
		+ 船名:育强
		+ 呼号:BOXZ
		+ 时间:0735UTC
		+ 船位:
		+ Inmarsat-C:441219018
		+ 通过C在0735UTC发射误报警，请取消
- 防止误报警的发生
    - 按钮放在不容易触碰的地方
    - 所有操作人员经过培训并持有相应的证书
    - 操作人员熟悉设备的操作
    - 张贴注意事项
    - 张贴误报警的取消方式和程序

## Part 7. MF/HF Radio Control Unit

### MF/HF Radio Control Unit 题卡1

#### 1. 解释面板按键与旋钮的功能

#### 2. 育强BOXZ在黄海水域航行，欲用高频无线电话经上海海岸电台联系上远公司(021-65701888)。从信号书中查出上海台的值守信道，并完成船-岸-用户无线电话通信

- NP281(2)查上海海岸电台的电话信道
- 选择一个高频信息(比如信道号818)并设置信道号818
- 拿起话机呼叫上海台
- 呼叫通了后，请上海台接通电话021-56701888
- 电话接通后，进行通话
- 通话完毕，通知上海台，然后挂机

### MF/HF Radio Control Unit 题卡2

#### 1. 将通信方式设置为Telex，收发频率设置为2174.5kHz

#### 2. 泰安海(BOAA)在青岛附近海域航行，经广州海岸电台完成船-岸-用户无线电话通信

### MF/HF Radio Control Unit 题卡3

#### 1. 快速设置无线电话国际遇险与安全通信频率

- 按1RT键3秒回到初始页面

#### 2. 甲、乙两船相距150海里左右，欲进行无线电话通信。编发一个中频DSC呼叫，预约通信方式和通信频率

- 按DSC键 - 打开DSC编辑菜单
- 编辑DSC呼叫序列的内容
- 发送

### MF/HF Radio Control Unit 题卡4

#### 1. 设置中/高频设备发射功率；开启噪声抑制

- 旋转旋钮到Hi处，按下旋钮选择High或Low
- 按5ACK/SQ键开启静噪功能

#### 2. 安龙江(BOUS)在长江口航行，在中频段呼叫上海海岸电台转接上远公司(021-56701888).从信号书中查出上海海岸电台的值守频率，并完成船-岸-用户无线电话通信

- 操作方法同题卡1第2题

### MF/HF Radio Control Unit 题卡5

#### 1. 将通信方式设置为AM Telephone，收发频率设置为2000kHz

- 按1RT键3秒回到初始页面
- 旋转旋钮到最左上角RT处
- 按下旋钮进入选择菜单
- 使用旋钮选择AM Telephone模式
- 按一次旋钮确认
- 再次旋转旋钮到Frequency处，按下旋钮进入输入状态
- 输入收发频率2000kHz
- 按一次旋钮确认

#### 2. 天昌海轮(3FCG4)在长江口锚地抛锚，使用中频与上海海岸电台进行无线电话通信测试

## Part 8. NBDP

### NBDP 题卡1

#### 1. 远吉轮(BJVL)在成山头附近发现3个漂浮集装箱，请编辑安全电文并存储

- 按F1 - 1New - 新建电文
    - Security Security Security
    - Three containers drifting near Chengshantou,ships in vicinity requested to keep sharp lookout
    - Master of MV Yuanji
- 再次按F1 - 3Save
- 选择Yes
- 输入文件名
- 按Enter保存

#### 2. 远吉轮(BJVL)将上述安全电文通告给附近的船舶

- F3 - 6 - FEC
- F3 - 0 - 选择频率2174.5kHz或8376.5kHz
- F3 - 9
    - Mode:FEC
    - ID:不用填
    - 按Enter
- Connect变色后
- F3 - 3
- 调出题1编辑妥的电文
- 按Enter发送
- 发送完成，按F10拆线，完成

### NBDP 题卡2

#### 1. 查看本船的应答码和选呼号

- 按F5
    - 5 Answer Back Code Entry - 查看本船应答码
    - 9 - 选呼号

#### 2. 天昌海轮(3FCG4)在青岛附近水域航行，查出上海海岸电台的电传呼号，选择最佳频率，完成通信测试

- 编辑海岸电台的信息
	* NP281(2),在后面目录索引找到电台名字，查找其对应的页码，翻到该页码，查看电台识别码(ID)及通信频率和相应信道
	* 按F5 - 1 - 选择Create或Change，按Enter
	* 在电台栏目中选择，以上海台为例
		+ Station:Shanghai Radio
		+ ID:2010
		+ Mode:ARQ FEC(根据需要选择相应的模式)
			+ 进行通信选择ARQ
			+ 接收或者广播选择FEC
		+ CH/Table:单频率选择Channel；多频率选择CH/Table
		+ Number:输入相应的信道号
	* 按Enter - OK
- 呼叫岸台，完成测试通信
	* 自动呼叫
		+ 编辑岸台
		+ 按F3 - 1
		+ 找到要呼叫的岸台，按Enter
		+ 接通后面板上的Connect会变色
	* 手动呼叫
		+ 按F3 - 6 - 设置接收方式为ARQ
		+ 按F3 - 0 - 设置通信频率
		+ 按F3 - 9 - 输入岸台应答码(上海台2010)
		+ 选择ARQ模式，按下Enter呼叫
		+ 接通后面板上的Connect会变色
- 叫通后
	* 岸台(以上海台2010为例)发送2010 XSG CN以及呼叫船舶的应答码等信息(显示在屏幕上)
	* 接着岸台会发送GA+?
	* 船台发送TST+(或者TEST+)
	* 岸台发送测试信息(显示在屏幕上)
	* GA+?
	* 船台按F10或发送BRK+
	* 结束测试

### NBDP 题卡3

#### 1. 请介绍主界面的菜单名称及功能

#### 2. 竹源轮(BOFO)航行在青岛港附近水域，查出广州海岸电台选呼号，选择最佳通信信道，完成与用户(david@soho.com)的email通信

- 前2个步骤与题卡2第2题类似，将上海台改成广州海岸电台
- 叫通广州海岸电台
	* 电台发送GA+?
	* 船台输入:EMAILDAVID/SOHO.COM+
	* 岸台发送:MSG+
	* 船台发送编辑好的电文:
		+ F3 - 3
		+ 选择要发送的电文
		+ Enter发送
		+ 岸台接收信息完成后，发送GA+?
		+ 船台发送BRK+或按F10
	* 完成信息的发送

### NBDP 题卡4

#### 1. 查看已接收到的电传电文

- F1 - Open

#### 2. 安龙江(BOUS)航行在青岛附近水域，查出信号书，选择最佳通信信道，并接收广州海岸电台发给本船的电传

- 查广州海岸电台的信息并编辑存入
	* 呼叫广州台，接通后
	* 船台发送:MSG+
	* 岸台转发电传信息，完成后GA+?
	* 船台发送:BRK+或按F10
	* 结束通信

### NBDP 题卡5

#### 1. 竹源轮(BOFO)航行于青岛附近水域，设置接收天津海岸电台播发的MSI

- 查找海岸电台的信息
	* NP283中，在后面目录索引找到电台名字，查找其对应的页码，翻到该页码，查看电台识别码，播发频率，播发信息的时间
- 到了播发时间，手动呼叫岸台
	* F3 - 6 设置接收方式为FEC
	* F3 - 0 设置通信频率
	* F3 - 9 输入岸台应答码2012,选择呼叫方式为FEC，Enter

#### 2. 乐泰轮(197** BOQB)航行于青岛附近水域，欲与航行于长江口附近的乐昌轮(197** BOQC)进行无线电传通信

- 呼叫船台
	* F3 - 6 - ARQ
	* F3 - 0 设置通信频率(日常通信不能使用遇险紧急频率)
	* F3 - 9 输入乐昌轮应答码(19702),ARQ,按Enter
	* 开始呼叫，接通后面板Connect变色
- 进行通信
	* 先交换应答码 - 按F7和F8
	* 发送信息
	* F3 - 3 找到编辑好的信息，按Enter发送
	* 若想让对方发送信息，按F9
	* 通信后按F10或输入BRK+结束

### NBDP 题卡6

#### 1. 查看NBDP的选呼号

- F5 - 8

#### 2. 天慧海轮(3FXB3)在青岛附近水域航行，经由上海海岸电台与陆地用户085330**进行直接电传通信。请查出岸台呼号，选择最佳通信频率，并完成通信

- 呼叫岸台
- 叫通后
- 岸台：GA+?
- 船舶：DIRTLX08533001+
- 岸台发送MOM+，发送一边陆地用户电传码，接线，接通后岸台发送GA+?
- 船舶：F3 -3 找到编辑好的信息，按Enter发送
- 发送完成，使用F7和F8交换应答码
- 船舶发送KKKK，与陆地用户拆线
- 岸台：GA+?
- 船舶:BRK+或按F10，结束通信

## Part 9. Navtex and Weather Fax

### Navtex and Weather Fax 题卡1

#### 1. 解释NAVTEX设备面板各功能键的作用

#### 2. 完成NAVTEX设备的自检测

- Menu - [6]System Diagnostics - [6]Self Test

#### 3. 查找日本JMH(Kagoshima)台气象大势分析图的播发频率和相关信息

- NP283(2) Page56

#### 4. 人工启动接收打印日本JMH(Kagoshima)台播发的气象大势分析图

- Ch - 001 - E - RCD

### Navtex and Weather Fax 题卡2

#### 1. 某NAVTEX报文的技术编码是RD00,解释此技术编码的含义

- R - 大连
- D - 搜救信息
- 00 - 接收信息的编号(00也是必须接收打印的信息)

#### 2. 天慧海轮(3FXB3)航行于南非好望角附近，设置NAVTEX播发台，接收N/W和W/X信息

#### 3. 解释气象传真件面板各功能键和旋钮的作用

#### 4. 接收的气象传真图倾斜，该如何调整

- SYNC旋钮
	* 左倾斜 - 向左旋转
	* 右倾斜 - 向右旋转

### Navtex and Weather Fax 题卡3

#### 1. 安宝江(BOAX)航行于渤海海域，从《Admiralty List of Radio Signals》中正确查找NAVTEX播发台的相关信息

#### 2. 查出信息后，正确设置NAVTEX播发台，并接收N/W和W/X信息

#### 3. 气象传真图的黑条不在两边如何调整

#### 4. 添加用户信道，信道号为711,用户名为QMC，频率为13900

### Navtex and Weather Fax 题卡4

- 题目丢失

# GMDSS评估题目 - 通信英语听力与会话题目

## Part 10. Speaking

### 1. *Please describe the main operational procedures and cautions should be taken when you call a coast station in radio telephony services.* 

When we call a coast radio station in radio telephony services, we must select the right equipments and frequencies according to the services and distance.

Select telephone mode on the radio equipment,Find out RT details of the coast radion station from the NP281,then set the correct frequency or channel,pick up the phone and push to the PTT to connect with the coast radio station,if you end the call you should say OUT and the hang up.

### 2. *Please describe what is urgency communication,the means used to transmit urgency communication,and the caution should be taken when urgency communicaton is transmit by operators at sea. What is safety communication?* 

When the vessel encountered urgency conditions,such as MOB,out of control,engine failure and so on. They are all the urgency communication.

Seafarers can use radio telephone,radio telex or Inmarsat SES to transmit urgency communication.

Urgency communication can only be transmitted under the authority of master,the information should contain urgency signal,ship's name,call sign,position,what's happened,need which kind of assistance and so on.

Safety communication is on the safe of the ship's communication such as transmit or receive MSI.

### 3. *Please describe the methods to protect the distress and safety frequencies.* 

In order to protect the distress and safety frequencies,the following should be noted:

- Avoiding harmful interference
- Prevention of unauthorized transmissions
- The transmissions which are not used for Distress and Safety purpose must be kept a minimum and,in the case of Ch16,be no more than 1 minute in duration
- And such transmissions may be used for call and relay at a low power.

### 4. *Please describe the alerting procedures in voice services in Inmarsat-F system* 

- Switch on the power supply
- Login appropriate ocean region
- Select appropriate coast earth station within the ocean region for communication
- Open the cover of the DISTRESS button and press it for 5 seconds
- Pick up the handset and waiting for RCC's answering
- When RCC answers,send distress alert on standard format. The MAYDAY alert should include the following information:
    - Ship's name
    - Call sign
    - Nature of distress
    - Ship's position
    - assistance required
    - other information useful for rescue
- Communication with RCC,receive instructions from RCC
- End of communication,put down the handset

### 5. *Describe watch keeping arrangements in SOLAS Chapter IV of 1988 amendment* [*Please elaborate the watch keeping arrangements made in the Chapter IV of the 1988 Amendments to 1974 SOLAS Convention(concerning communication of GMDSS)*]

According to the SOLAS Chapter IV,GMDSS station should keep watch on the frequencies as follows:

- VHF DSC keep watch on Ch70
- MF DSC keep watch on 2187.5kHz
- MF/HF DSC keep watch on 2187.5kHz,8414.5kHz and one of other HF DSC frequencies
- And keep watch on the frequencies for receiving MSI
- For Inmarsat terminal equipped vessel,keep Inmarsat terminal in operation for receiving distress alert from shore to ship

### 6, *Describe the actions you will take when you,an operator on board,receive an alert at sea* 

When I receive an alert at sea,I will:

- Report to master at once
- Tune the transmitter and reveiver on appropriate frequencies and select proper communication mode
- Keep continuous watch on the frequency on which the distress communication is going on
- Prepare to take part in distress communication,in accordance with radio regulations and under master's order
- Make a good record of the distress communication in logbook

### 7. *Describe the proper way of using VHF* 

When using VHF,the following should be noted:

- the lowest transmitter power necessary for satisfactory communication should be used
- avoid superfluous transmission
- routine call should not be carried out in silence period
- standard marine communication phrase should be used
- the called ship indicates channel for subsequence communication
- distress call or message are carried out on channel 16,and have absolute priority over all other communications
- routine call and reply on channel 16 should not last more than one minute

### 8. *Please describe the procedures of sending distress message by using Inmarsat-C terminals* 

In emergency situation:

- switch on the power supply
- login appropriate ocean region
- select column "distress" in the main menu
- select appropriate LES
- select the nature of distress
- then press the distress button at least 4 seconds to transmit alert

If time permit:

- switch on the power supply
- login appropriate ocean region
- edit a distress alert message and save it in the memory
- select the "transmit" memu,open the "Transmit Message" window,select the priority "distress"
- select a suitable LES for communication
- select the distress message to be transmitted
- move the cursor to "Transmit",press "ENTER" key on the keyboard to transmit the alert
- waiting for RCC's answering

### 9. *What information is transmitted in a DSC dirstress alert?* 

The following information is transmitted in a DSC distress alert:

- Category:distress
- MMSI of the ship in distress
- Nature of distress
- Position of distress
- The valid time of the position in UTC
- Method of subsequent communication

### 10. *What daily,weekly and monthly checks should you perform about GMDSS?* 

Daily checks is about DSC self test

Weekly checks is about DSC link test

Monthly checks are about two way VHF radio telephone test,the battery as reserve source of energy test and SART test

### 11. *NAVTEX is used for receiving what type of information?* 

NAVTEX receiver is a Narrow Band Direct Printing device operating on the frequency 518 Khz. and is a vital part of GMDSS. It is automaticlly receives MSI such as navigational warnings,meteorological warnings,meteorological forecast. Piracy Warnings,search and rescue information and so on

### 12. *What means of identification is used by DSC?* 

If a station sends a DSC call to another,the two stations can use the 9-digits MMSI to identify each other. When transmitting or receiving DSC call,if the number indicated is:

- 00+(plus)+MID+4 digits select call number,the coast station call will be identified
- 0+(plus)+MID+5 digits select call number,the group call will be identified
- MID+6 digits select call number,the ship station call will be identified

### 13. *You receive a distress relay for a vessel within your vicinity,what actions would you take?* 

When a distress relay for a vessel within my vicinity is received,in accordance with the radio regulations,if necessary,on the authority of master:

- First,I should acknowledge the receipt of distress relay by radiotelephone on the distress frequency in the same band on which the distress relay message is received
- Then,I should get in contact with the coast station who send the distress relay
- And do my best to contact with the distress vessel,and prepare for assist the distress vessel according to master's instructions

### 14. *If you are the operator onboard as general cargo ship,which is named as Fenghuangshan,you received a DSC alert on channel 70 when you are sailing in the sea area A1,what will you do with the alert?(the ship's name:Tulip,MMSI:4631123456,position:3821N 13843E,nature of distress:collision)* 

When I receive a DSC alert on ch70 at sea area A1,I will wait for the acknowledgement from the coast station,and change to ch16 for listening to the subsequent distress communications

And report the incident to the master at once

If the vessel in distress is in the vicinity of me,on the authority of master,I will acknoledge the receipt as soon as possible by radiotelephone on ch16

And contact with the coast station for further instructions

Enter the details of distress traffic into the log book

### 15. *If you are the operator onboard a chemical tanker,whose name is iceland poppy. You are on fire,and the abandon ship order is given by the captain.please introduce your task and explain its ingredients in that case* 

My task is to transimit a distress alert and distress communications.When the abandon ship order is given,the following steps should be performed:

- Sending a DSC alert at once
- Boarding to the life saving boat with EPIRB/SART/Two way radio,and radio log,as well as the station license in hand
- When boarding the life boat,activate the EPIRB,switch on the SART and mount the SART as high as possible 
- Switch on the Two way radio and stand by on channel 16 for on-scene communications

### 16. *If you are the operator on board a bulk vessel,which run aground at 1645UTC at position 2605S 10417W (in the sae area A1). Please describe the altering procedures in the terrestrial systems.(Your ship's name is Yufeng)* 

First,use VHF Ch70 to send a distress call,then send a Mayday message on VHF Ch16:

- Mayday Mayday Mayday
- This is Yufeng Yufeng Yufeng
- Mayday Yufeng BBGL
- position:
    - latitude: two six degrees zero five minutes south
    - longitude: one zero four degrees one seven minutes west
- I am aground
- request assistance immediatelly
- over

### 17. *Describe how to coordinate with the give-way vessel by VHF in crossing situation.*

Stand-on vessel:MV GATE,course 030 degrees,speed 15 knots

Give-way vessel:MV START,course 170 degrees,speed 18 knots,pass port to port

How to change VHF channel?

How to identify the calling vessel?

How to coordinate the passing actions in crossing situation? 

- Security Security Security
- MV STAR STAR STAR
- This is GATE GATE GATE calling,please change to ch13,over 
- MV GATE,this is MV STAR,change to ch13,over
- MV STAR,this is MV GATE,coming please,over
- MV GATE,this is MV STAR,go ahead please,over
- MV STAR,this is MV GATE,I am stand-on vessel,my course is 030 degrees and speed is 15 knots.You are give-way vessel,what is your course and speed? over
- MV STAR,this is MV GATE,please slow down your speed and alter your course to starboard,pass port to port,over 
- MV GATE,this is MV STAR,roger,I will slow down my speed and alter course to starboard,pass port to port,over
- MV STAR,this is MV GATE,thank you,keep contact this channel,out

### 18. *If you are the operator onboard a general cargo ship,whose name is COTON TREE,provides your vessel is disabled at position 1725N 3521W,please warn vessels in your vicinity to keep clear of you.(drifting speed 2 knots,direction 090 degrees)* 

- Security Security Security
- All ships All ships All ships
- This is MV COTON TREE COTON TREE COTON TREE
- Serurity MV COTON TREE BXYZ
- I am disabled at position 1725N 3521W,driftig speed 2 knots direction 090 degrees
- Request all ships keep clear
- Over

### 19. *There is floating ice in position 4700N 5000W,it is dangerous to navigating,Banks Radio let Yuqiang(Callsign:YUQI) keep clear of it,Yuqiang will do as advised* 

Please make a safety communication.The safety signal Security.This is + the name of the station transmitting the safety message.The text of the message:

(B-Banks Radio;Y-Yuqiang)

- B:Security Security Security
- MV Yuqiang Yuqiang Yuqiang
- This is Banks Radio,Banks Radio Banks Radio
- Security Banks Radio
- Navigational warning
- There is floating ice in position 4700N 5000W.It is dangerous to navigation
- You must navigate with caution and keep clear of it
- Over

- Y:Security
- Banks Radio
- This is MV Yuqiang YUQI
- Navigational warning received.I will follow your advice.thank you
- Over and out

### 20. *Taoyuanhai(BSJX) is in collision with a fishing boat at 3004N 12020E and sinking,please send a distress alert* 

The distress signal Mayday,which is read for three times

This is + the name of the vessel in distress,which is read for three times

The call sign and other identification

The nature of distress

- Mayday Mayday Mayday
- This is Taoyuanhai Taoyuanhai Taoyuanhai
- Mayday Taoyuanhai BSJX
- Position:
    - latitude:3004N
    - longitude:12020E
- Collision with fishing boat,sinking
- Request:immediate assistance
- Over

### 21. *Yuying(YUYG)'s main engine is broken down severely,Shanghai Radio station will send a tug for her,they are going on the urgency traffic'* 

Vessel in urgency:the urgency signal Panpan,which is read for three times

This is + the name and call sign of the vessel in urgency

Shanghai Radio:the urgency signal Panpan

The necessary information

Tug will be made fast on port bow

- Panpan Panpan Panpan
- Shanghai Radio Shanghai Radio Shanghai Radio
- This is Yuying Yuying Yuying
- Panpan Yuying YUYG
- Position:090 degrees 5 miles from No1 light vessel
- My main engine is broken down severely
- Require tug assistance immediately
- Over

- Panpan
- Yuying Yuying Yuying
- This is Shanghai Radio
- Panpan received
- A tug is coming to your assistance.Please get towing line ready,the tug will be made fast on your port bow
- Over

### 22. *Give an example of a Mayday call* 

- Mayday Mayday Mayday
- This is Taoyuanhai Taoyuanhai Taoyuanhai
- Mayday Taoyuanhai BSJX
- Position:
    - latitude:3004N
    - longitude:12020E
    - Collision with fishing boat,sinking
    - Request:immediate assistance
    - Over

### 23. *Taoyuanhai(BSJX) sends a distress alert,Yuqiang(BQRS) acknowledges the receipt of the distress alert* 

The distress signal Mayday

The name followed by the call sign of the station sending the distress message and the station acknowledging receipt

Received Mayday

- Mayday Mayday Mayday
- This is Taoyuanhai Taoyuanhai Taoyuanhai
- Mayday Taoyuanhai BSJX
- Position:
    - latitude:3004N
    - longitude:12020E
- Collision with fishing boat,sinking
- Request:immediate assistance
- Over

### 24. *Send a Panpan message according to the given information* 

ship's name:Blue Sea

call sign:BERN

distress position:2204N 12708E

nature of distress suffered:break down of steering gears

assistance required:convoy

- Panpan Panpan Panpan
- This is MV Blue Sea Blue Sea Blue Sea
- Panpan MV Blue Sea BERN
- My steering gear is broken down in position 2204N 12708E
- Require convoy assistance
- Over

### 25. *Yuqing(YOBK) has a man ill and is ready for helicopter,she will identify herself by directing signal lamp at helicopter,they are going on the urgency traffic* 

vessel in urgency:the distress(urgency) signal Panpan,which is read for three times

this is + the name and call sign of the vessel in distress(urgency)

helicopter:the distress(urgency) signal Panpan

the necessary information

- Panpan Panpan Panpan
- This is MV Yuqing Yuqing Yuqing
- Panpan MV Yuqing YOBK
- Position:090 degrees true bearing 50 miles from Chongming Island
- I has a man ill seriously on board vessel
- Require helicopter assistance
- I am ready for the helicopter
- Over

- Panpan
- MV Yuqing this is helicopter
- I am coming to your assistance
- Please identify yourself by directing signal lamp
- Over

- Panpan
- Helicopter this is MV Yuqing
- Roger
- I will identify myself by directing signal lamp
- Over

### 26. *Minghua(BJWK) is in distress,Yuqiang(BBGD) sends a rescue information:her position at 1430 GMT is 3604N 2005E,speed is 18 knots,ETA is 1530GMT* 

Minghua affirms it

The distress signal Mayday

This is + the name and call sign of the vessel in distress

Repeat the information of the rescue station

- Mayday
- Minghua This is Yuqiang BBGD
- Received Mayday
- Position:
   - latitude:3604N
   - longitude:12005E
- Time:1430GMT
- Speed:18knots
- ETA:1530GMT
- Over

- Mayday
- Yuqiang this is Minghua BJWK
- Understood
- Position:
    - latitude:3604N
    - longitude:12005E
- Time:1430GMT
- Speed:18 knots
- ETA:1530GMT
- Over

### 27. *Yinhe(BOLR) is on fire and has dangerous cargo on board at 3604N 12020E,and sends a distress alert at 1400GMT.Yuqiang(BQRS) relays the distress call to all station at 1415GMT* 

the distress signal Mayday Relay,which is read three times.All stations or coast station name,as appropriate,which is read three times

- Mayday Mayday Mayday
- This is Yinhe Yinhe Yinhe
- Mayday Yinhe BOLR
- Position:
    - latitude:3604N
    - longitude:12020E
- Distress time:1400GMT
- I am on fire and has dangerous cargo on board
- Request:immediate assistance
- Over

- Mayday Relay Mayday Relay Mayday Relay
- This is Yuqiang Yuqiang Yuqiang BQRS
- Following received from Yinhe
- Time 1415GMT

- Mayday
- Yinhe BOLR
- Position:3604N 12020E
- Distress time:1400GMT
- I am on fire and has dangerous cargo on board
- Request:immeidate assistance
- This is Yuqiang
- Over

## Part 11 Question and Answer

### 1. *Coastal radio station keep a constant watch on distress frequencies.What frequencies are they?* 

Ch70,2M,8M and also on at least one of frequencies 4M,6M,12M or 16M

### 2. *How many times should the distress signal "Mayday" be spoken when sending a distress alert by radiotelephony?* 

Three times

### 3. *what does Mayday means in marine communications?* 

It is distress signal in marine communications

### 4. *Which channel is designated for VHF DSC alerting?* 

Channel 70 is designated for VHF DSC alerting

### 5. *What should a station do when transmitting an inadvertent distress alert or call?* 

A station should send a message to RCC to cancel false distress alert

### 6. *What should be included in Mayday message?* 

Mayday message should be included:

- distress signal
- ship's name
- call sign
- position
- nature of distress
- time
- assistance type

### 7. *Which parties are those on-scene communications carried out between?* 

On-scene communications carried out between distress ship and rescue units

### 8. *Who should be addressed to when acknowledging the receipt of a distress alert sent by DSC?* 

The vessel in distress

### 9. *What should a signal be prefixed by for distress traffic by radiotelephony?* 

Mayday Mayday Mayday

### 10. *According to the SOLAS,which radio equipment is not necessary for the ships sailing at sea area A2?* 

HF radio equipment and Inmarsat SES is not necessary for the ships sailing at sea area A2

### 11. *Shall an urgency communication have priority over all other communications except distress?* 

Yes,it should be

### 12. *Which means is often used to provide vessel's position information to the GMDSS equipment?* 

GPS provides position information to the GMDSS equipment

### 13. *How many times should the urgency signal "Panpan" be spoken when sending an urgency call?* 

Three times

### 14. *What's an urgency signal prefixed by for sending an urgency call?* 

Panpan Panpan Panpan

### 15. *Relatinng the reserve source of engergy,if it is not a battery,what is the period of test?* 

The period of test is a week

### 16. *What does Security means in marine communications?* 

It is Safety signal in marine communications

### 17. *How many times should the safety signal "Security" be spoken when send a safety call?* 

Three times

### 18. *What does the safety call format or the safety signal indicate?* 

The safety signal is Security,must be spoken three times

### 19. *Which mode is normally used when carrying out safety communications by NBDP?* 

FEC mode

### 20. *What kind of things should be reported to the pilot station?* 

The pilot station should be reported ETA,vessel's particular(LOA,draft) and so on

### 21. *When the vessel enters the VTS area,what is usually requested to report?* 

- ship's name
- call sign
- destination
- come from which port
- ETA
- the port of call

### 22. *What does "fairway speed" mean?* 

The fairway speed is the vessel pass this fairway limited speed

### 23. *What is the meaning of "ETD"?* 

Estimated time of departure

### 24. *what should be confirmed from the pilot station?* 

The pilot station should confirm POB time,which side is the pilot ladder rigged and how many meters above water

### 25. *How can a ship get in touch with a port before her arrival?* 

Ships can get in touch with port via VHF telephone,MF/HF telephone or Inmarsat F and so on

### 26. *What shuold a master do before sailing?* 

Master must make sure all the formalities are signed and the vessel is suitable for sailing

### 27. *Please spell your ship's name and call sign?* 

Yuqiang/BOXZ(Using Code language)

Yankee Uniform Quebec India Alpha November Golf

Bravo Oscar X-ray Zulu

### 28. *What does MRCC stand for and what is its function?* 

MRCC stand for Maritime Rescue Coordination center.Its function is for coordinating search and rescue at sea

### 29. *What is general cargo?* 

Such as corn,iron ore and so on

### 30. *What's your present speed and course?* 

My present speed is 10 knots and course is 125 degrees

### 31. *In accordance with the SOLAS Convetion,what is the area outside sea area A1 A2 A3?* 

It is sea area A4

### 32. *Should a ship station in receipt of urgency call address her acknowledgement to all other sations?* 

No,she shouldn't

### 33. *Relating DSC facilities,what is the period of self test?* 

The period of self test is each day

### 34. *Can a RCC(rescue coordination centre) coordinating distress traffic impose silence on station which are interfeing with the distress traffic?* 

Yes,it can be

### 35. *What is an emergency signal fixed by?* 

An emergency signal is fixed by urgency signal Panpan,spoken three times

### 36. *What does Panpan mean in marine communication?* 

Panpan means to announce urgency message

### 37. *When a station transmitting or intervening ...,what does distress alert do?* 

The station interfering with distress traffic will be imposed to keep radio silence

another answer: The distress station or on-scene commander will say "Silence Mayday" to impose the station interfering with distress traffic to keep radio silence

### 38. *Coastal radio stations keep a constant watch on distress frequencies,what frequencies are they?* 

Coastal radio stations keep a constant watch on the following distress frequencies:

- 156.525 Mhz
- 2187.5 Khz
- 4207.5 Khz
- 6312.0 Khz
- 8414.5 Khz
- 12577.0 Khz
- 16804.5 Khz

### 39. *What does SOLAS stand for?* 

SOLAS stands for international convention for the Safety Of Life At Sea

### 40. *What does STCW stand for?* 

STCW stands for international convention on Standards of Training,Certification and Watch keeping for seafarers

### 41. *What is the appropriate range of MF radio waves during the day time?* 

During the day time,the approximate ranger of MF radio waves is about 100 miles

### 42. *Who should be addressed to when acknowledging the receipt of a distress alert sent by DSC?* 

When acknowledging the receipt of a distress alert sent by DSC,we address the acknowledgement to all stations

### 43. *How many times should the distress signal Mayday Relay be spoken when relaying a distress alert by radiotelephony?* 

When relaying a distress alert by radiotelephony,the distress signal Mayday Relay should be spoken three times

### 44. *In which sea areas,is it out of question that you can obtain Inmarsat services?* 

At sea area A3,it is out of question that I can obtain Inmarsat services

### 45. *What should a station do when transmitting an advertent distress alert or call?* 

When a station transmitting an advertent distress alert or call,the operator should stop the transmitting and make a cancellation to the associated RCC

## Part 12 Reading

### 1.
The proper use of VHF channel at sea makes an important contribution to navigational safety. In accordance with the ITU Radio Regulations:

- Channel 16(156.8 Mhz) may only be used for distress,urgency and very brief safety communications and for calling to establish communications which should then be conducted on a suitable working channel
- On VHF channel allocated to the port operations service the only messages permitted are restricted to those relating to the operational handling,the movement and safety of ships and,in emergency,to the safety of persons. The use of these channels for ship-to-ship communications may cause serious interference to communications related to the movement and safety of shipping in congested port areas
- VHF equipment is frequently operated by persons not trained in its proper use though the ITU Radio Regulations require that the service of every ship radiotelephone station shall be controlled by an operator holding a certificate issued or recoginzed by the Government concerned

### 2.

Store-and-forward messaging services:

The Inmarsat-C network can be used for sending different types of store-and-forward messages:

- Telex message service: you can send and receive messages between your MES and any telex terminal connected to the national/international telex network
- Fax messages service: this allows an MES to send text messages to a shore-based fax machine. It is not possible for a shore-based fax user to send messages directly to an MES. A fax message can only be send as a text message via a fax bureau service
- Messages to and from a computer: you can send and receive messages between your MES and any computer terminal connected to the PSTN or PSTN newwork. For shore-to-ship traffic you need to be registered with an Inmarsat service provider to get access to the service required
- Electronic mail(email) service: messages can be send via either the Internet or hub services
- Dedicated data processing systems connected via a private network(such as a leased line)
- Ship-to-ship comunications
- Shore acces coe or 2-digit code messaging

### 3.

The operator also has control over current and planned NAVAREA/METAREA and coastal service coverage areas for which the MSI information is required.The options that may be pre-programmed into a MES are indicated below:

- MES's position
- Current and planned NAVAREA/METAREA
- Current and planned coastal service converage area
    - The ship's position on the MES may be entered automatically from an external navigation aid or integrated GPS receiver or may be entered manually. It is recommended that the ship's position be updated at least every four hours. If the ship's position has not been updated for more than 12 hours,all SafetyNet messages with priority higher than routine within the entire ocean region will be received and printed
- When preparing a message for broadcast,the information provider includes addressing information which specifies the area in which the message is to be received.The address may specify one of the following:
    - EGC receivers within an open network,such as all ships within a given geographical area.The area could be a specifc NAVAREA/METAREA,a circle around a vessel in distress,a rectangular area or coastal area
    - EGC receivers within a closed newwork,for example,all ships belonging to a fleet,identified by a single ENID code
    - Individual EGC receivers
    - All EGC receivers in an ocean region

### 4.

It is crucial that 406 Mhz distress beacons be registered in recognized beacon registration data bases which will be accessible to search and rescue authorities at all times. The information contained in these data bases concerning the beacon,its owner,and the vehicle/vesse on which the beacons is mounted is vital for the effective use of Search and Rescue resources. The proper registration of a beacon could make the difference between success and failure of a search and rescue mission

You will need the following information to register a beacon:

- Beacon Hexadecimal Indentification(15 Hexadecimal characters)
- Owner name and phone number
- Emergency contact name and phone number
- Vehicle type(selectable from a menu)
- Vehicle name,MMSI,call sign or identificaiton number(except for PLBs)

### 5.

ARQ means Automatic Repetition reQuest and provides error detection and error correction. However, it requires both communication stations to have their respective transmitters and recerivers active simultaneously

This mode is normally restricted in use between two stations eg. a ship and a coast station or perhaps two ships

FEC means Forward Error Correction and provides error detection only. If any doubtful letters occur in the text,a gap(or sometimes an asterisk) will appear. With FEC the receiving station(s) do not need an active transmitter. This mode of operation is therefore ideal for broadcasting information to numberous stations simultaneously and it is used for sending traffic lists,weather and navigational warnings etc. It is therefore sometimes referred to as the "Broadcast mode" and is the preferred telex mode for distress,urgency and safety messages

A derivation of FEC is called SELFEC. Again the recipient's transmitter does not have to be active and it is similar to FEC in all respects except that the transmission is addressed to a particular receiving station(ie. by addressing the call to the appropriate selcall number). It is an ideal mode of transmission for ships to receive telex messages whilst in a port where the use of transmitters may be restricted or forbidden

### 6.

The Inmarsat system provides priority access to satellite communications channel in emergecy situations. Each MES is capable of initiating a request message with distress priority. Any request message with a distress priority indication is automatically recognized at the LES and a satellite channel is instantly assigned. If all satellite channels happen to be busy,one of them will be pre-empted and allocated to the MES which initiated the distress priority call. The processing of such calls is completely automatic and does not involve any human intervetions. The LES personnel,however,are notified of the receiption and passing through of a distress priority message by audio/visual alarms 

To ensure the correct treatment of distress priority request the NCS in each ocean region automatically monitors the processing of such calls by all other LESs in that region. In the event that any anomalies in processing are detected,the NCS will take appropriate action for the establishment of the end-to-end connections. In the distress priority message and automaticall accepts the call if an identity of a non-operational LES has been detected(which may happen due to operator error aboard the vessel in distress)

### 7.

A DSC distress alert may be sent as a "single frequency" or "multi-frequency" attempt. At MF and HF,distress alert attemps may be transmitted either as single frequency or multi-frequency call attempts

When using the "single frequency" method, a 7.2 second sequence consisting of a dot pattern phasing sequence,the call content(containing the basic distress information) and a closing sequence is automatically sent 5 times in a single uninterrupted burst. This is both for error correction purposes and to increase the probability that it will be received correctly on the first attempt. A 1.8 second expansion message containing more detailed information should than be sent without a break after the 5th alerting sequence(ie. up to 38 seconds in all)

When using "multi-frequency" method, the 7.2 seconds sequence followed by the 1.8 second expansion message is sent on up to six frequecies in quick succession

The frequencies selected for multi-frequency call attempt should always include the 2 Mhz and 8 Mhz bands plus at least one other. The individual distress alerting sequences used for multi-frequency distress alert attempt take 9 seconds to transmit as each one comprises the 7.2 seconds alerting sequence followed by the 1.8 seconds "expansion sequence"

### 8.

The distress priority applies not only with respect to satellite channels but also to the automatic routine of the call to the appropriate rescue authority. Each LES in the system is required to provide reliable telephone and telex interconnection with a rescue coordination center(RCC). These national rescue centers are usually known as associated RCCs. The means of LES-RCC interconnection may vary from country to country and may include use of dedicated lines or public swtiched networks. Thus,any distress priority request message received at the LES is automatically processed and passed to the associated RCC. Some LESs,due to national considerations,pass distress priority messages to special operators,who are responsible for the subsequent routing of the call to the appropriate RCC or provide an option which allows the shipboard operator to contact any RCC when a satellite channel has been assigned on the distress priority basis

The initiation of a distress priority message in most MESs is made simple for ship crew members by provision of a distress button or code in the MES. This single operation,a push of the distress button provides automatic,direct and assured connection to a competent rescue authority. This avoids the need for the MES operator to select or key the telex or telephone number of the RCC thereby eliminating possible human error

### 9.

Before transmitting,think about the subjects which have to be communicated and,if necessary,prepare written notes to avoid unnecessary interruptions and ensure that no valuable time is wasted on a busy channel

Listen before commencing to transmit to make certain that the channel is not already in use. This will aviod unnecessary and irritating interference

VHF equipment should be used correctly and in accordance with the radio regulations. The following in particular should be avoided:

- calling on channel 16 for purpose other than distress,urgency and very brief safety communications when another calling channel is available
- communications not related to safety and navigation on port operation channels
- non-essential transmissions,eg. needless and superfluous signals and correspondence
- transmitting without correct identification
- occupation of one particular channel under poor conidtions
- use of offensive language
- repetition of words and phrases should be avoided unless specifically requested by the receiving station
- When possible,the lowest transmitter power necessary for saticfactory communication should be used

### 10.

The nominal system configuration comprises four satellites,two COSPAS and two SARSAT

Russia supplies two COSPAS satellites placed in near-polar orbits from 700 to 1000 km altitude and equipped with SAR instrumentation at 121.5 Mhz and 406 Mhz

The USA supplies two NOAA meteorological satellites of the SARSAT system placed in sun-synchronous,near-polar orbits at about 850 km altitude,and equipped with SAR instrumentation at 121.5 Mhz and 406 Mhz suppled by Canada and France

Each satellite makes a complete orbit of the earth around the poles in about 100 minutes,traveling at a velocity of 7 km per second. The satellite views a "swatch" of the earth over 6000 km wide as it circles the globe,giving an instantaneous "field of view" about the size of a continent. When viewed from the earth,the satellite crosses the sky in about 15 minutes,depending on the maximum elevation angle of the particular pass
