# Manjaro安装VirtualBox

## 1. 查看系统内核版本

```bash
❯ uname -rs
Linux 5.8.18-1-MANJARO
```
## 2. 安装VirtualBox

根据内核版本选择相应的模块

```bash
❯ sudo pacman -S virtualbox
正在解析依赖关系...
:: 有 11 个软件包可提供 VIRTUALBOX-HOST-MODULES ：
:: 软件仓库 extra
   1) linux414-virtualbox-host-modules  2) linux419-virtualbox-host-modules  3) linux44-virtualbox-host-modules  4) linux49-virtualbox-host-modules
   5) linux54-virtualbox-host-modules  6) linux57-virtualbox-host-modules  7) linux58-virtualbox-host-modules  8) linux59-virtualbox-host-modules
:: 软件仓库 community
   9) linux54-rt-virtualbox-host-modules  10) linux59-rt-virtualbox-host-modules  11) virtualbox-host-dkms

输入某个数字 ( 默认=1 ): 7
正在查找软件包冲突...

软件包 (2) linux58-virtualbox-host-modules-6.1.16-3  virtualbox-6.1.16-1

下载大小：   35.52 MiB
全部安装大小：  161.15 MiB

:: 进行安装吗？ [Y/n] y
:: 正在获取软件包......
 linux58-virtualbox-host-modules-6.1.16-3-x86_64             182.3 KiB  4.45 MiB/s 00:00 [####################################################] 100%
 virtualbox-6.1.16-1-x86_64                                   35.3 MiB  4.09 MiB/s 00:09 [####################################################] 100%
(2/2) 正在检查密钥环里的密钥                                                             [####################################################] 100%
(2/2) 正在检查软件包完整性                                                               [####################################################] 100%
(2/2) 正在加载软件包文件                                                                 [####################################################] 100%
(2/2) 正在检查文件冲突                                                                   [####################################################] 100%
(2/2) 正在检查可用存储空间                                                               [####################################################] 100%
:: 正在处理软件包的变化...
(1/2) 正在安装 linux58-virtualbox-host-modules                                           [####################################################] 100%
===> You must load vboxdrv module before starting VirtualBox:
===> # modprobe vboxdrv
(2/2) 正在安装 virtualbox                                                                [####################################################] 100%
virtualbox 的可选依赖
    vde2: Virtual Distributed Ethernet support
    virtualbox-guest-iso: Guest Additions CD image
    virtualbox-ext-vnc: VNC server support
    virtualbox-sdk: Developer kit
:: 正在运行事务后钩子函数...
(1/8) Creating system user accounts...
Creating group vboxusers with gid 108.
(2/8) Reloading system manager configuration...
(3/8) Reloading device manager configuration...
(4/8) Arming ConditionNeedsUpdate...
(5/8) Updating module dependencies...
(6/8) Updating icon theme caches...
(7/8) Updating the desktop file MIME type cache...
(8/8) Updating the MIME type database...

```
