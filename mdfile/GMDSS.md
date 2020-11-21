[toc]
# GMDSS评估题目

## Part 1. IMARSAT-C

### 题卡1

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

### 题卡2

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

### 题卡3

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

### 题卡4

#### 1. 解释MES主菜单各项的功能

#### 2. C站设有保安报警，与遇险报警有何区别？




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
- When possibel,the lowest transmitter power necessary for saticfactory communication should be used

### 10.

The nominal system configuration comprises four satellites,two COSPAS and two SARSAT

Russia supplies two COSPAS satellites placed in near-polar orbits from 700 to 1000 km altitude and equipped with SAR instrumentation at 121.5 Mhz and 406 Mhz

The USA supplies two NOAA meteorological satellites of the SARSAT system placed in sun-synchronous,near-polar orbits at about 850 km altitude,and equipped with SAR instrumentation at 121.5 Mhz and 406 Mhz suppled by Canada and France

Each satellite makes a complete orbit of the earth around the poles in about 100 minutes,traveling at a velocity of 7 km per second. The satellite views a "swatch" of the earth over 6000 km wide as it circles the globe,giving an instantaneous "field of view" about the size of a continent. When viewed from the earth,the satellite crosses the sky in about 15 minutes,depending on the maximum elevation angle of the particular pass
