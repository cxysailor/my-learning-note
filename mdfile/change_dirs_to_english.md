### Manjaro中将文件夹改为英文

## 1. 安装xdg-user-dirs-gtk

```bash
❯ sudo pacman -S xdg-user-dirs-gtk
[sudo] cxy 的密码：
正在解析依赖关系...
正在查找软件包冲突...

软件包 (1) xdg-user-dirs-gtk-0.10+9+g5b7efc6-3

下载大小：  0.05 MiB
全部安装大小：  0.17 MiB

:: 进行安装吗？ [Y/n] y
:: 正在获取软件包......
 xdg-user-dirs-gtk-0.10+9+g5b7efc6-3-x86_64                               50.6 KiB   303 KiB/s 00:00 [###########################################################] 100%
(1/1) 正在检查密钥环里的密钥                                                                         [###########################################################] 100%
(1/1) 正在检查软件包完整性                                                                           [###########################################################] 100%
(1/1) 正在加载软件包文件                                                                             [###########################################################] 100%
(1/1) 正在检查文件冲突                                                                               [###########################################################] 100%
(1/1) 正在检查可用存储空间                                                                           [###########################################################] 100%
:: 正在处理软件包的变化...
(1/1) 正在安装 xdg-user-dirs-gtk                                                                     [###########################################################] 100%
:: 正在运行事务后钩子函数...
(1/1) Arming ConditionNeedsUpdate...
```

## 2. 切换到英文

```bash
❯ export LANG=en_US
```

## 3. 执行更新命令

出现的提示对话框中点击**Update Names**

```bash
❯ xdg-user-dirs-gtk-update

(process:3398): Gtk-WARNING **: 22:21:00.545: Locale not supported by C library.
        Using the fallback 'C' locale.
Moving DESKTOP directory from 桌面 to Desktop
Moving DOWNLOAD directory from 下载 to Downloads
Moving TEMPLATES directory from 模板 to Templates
Moving PUBLICSHARE directory from 公共 to Public
Moving DOCUMENTS directory from 文档 to Documents
Moving MUSIC directory from 音乐 to Music
Moving PICTURES directory from 图片 to Pictures
Moving VIDEOS directory from 视频 to Videos
```

## 4. 切换到中文

若出现提示，则点击**Keep Old Names**

```bash
❯ export LANG=zh_CH
```
