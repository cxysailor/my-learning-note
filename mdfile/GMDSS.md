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

### 17. *Describe how to coordinate with the give-way vessel by VHF in crossing situation* 

