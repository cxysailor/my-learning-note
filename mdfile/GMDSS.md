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


