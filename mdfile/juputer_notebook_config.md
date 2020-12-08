# Jupyter Notebook

## 1. Installation

```bash
❯ sudo pacman -S jupyter-notebook
[sudo] cxy 的密码：
正在解析依赖关系...
正在查找软件包冲突...
警告：检测到循环依赖：
警告：python-ipykernel 将在它 python-jupyter_client 的依赖关系之前被安装
警告：检测到循环依赖：
警告：jupyter-widgetsnbextension 将在它 jupyter-notebook 的依赖关系之前被安装

软件包 (43) ipython-7.19.0-1  jupyter-4.6.3-1  jupyter-nbconvert-5.6.1-1  jupyter-nbformat-5.0.6-1  jupyter-widgetsnbextension-1:3.5.1-1
            jupyter_console-6.2.0-1  mathjax2-2.7.9-1  python-argon2_cffi-20.1.0-1  python-attrs-20.3.0-1  python-backcall-0.2.0-1
            python-bleach-3.2.1-1  python-dateutil-2.8.1-3  python-decorator-4.4.2-1  python-defusedxml-0.6.0-4  python-entrypoints-0.3-3
            python-importlib-metadata-2.0.0-1  python-ipykernel-5.3.4-1  python-ipywidgets-7.5.1-4  python-jedi-0.17.2-1  python-jinja-2.11.2-2
            python-jsonschema-3.2.0-2  python-jupyter_client-6.1.7-1  python-jupyter_core-4.6.3-2  python-markupsafe-1.1.1-4
            python-mistune-0.8.4-3  python-pandocfilters-1.4.3-1  python-parso-1:0.7.1-1  python-pexpect-4.8.0-1  python-pickleshare-0.7.5-3
            python-prometheus_client-0.8.0-2  python-prompt_toolkit-3.0.8-1  python-ptyprocess-0.6.0-4  python-pygments-2.7.2-1
            python-pyrsistent-0.17.3-1  python-pyzmq-19.0.1-2  python-send2trash-1.5.0-4  python-terminado-0.9.1-1  python-testpath-0.4.4-1
            python-tornado-6.1.0-1  python-traitlets-4.3.3-3  python-wcwidth-0.2.5-1  python-zipp-3.4.0-1  jupyter-notebook-6.1.4-1

下载大小：   17.52 MiB
全部安装大小：  103.99 MiB

:: 进行安装吗？ [Y/n] y
:: 正在获取软件包......
 python-markupsafe-1.1.1-4-x86_64                             24.4 KiB  2.38 MiB/s 00:00 [####################################################] 100%
 python-attrs-20.3.0-1-any                                    72.5 KiB  2.62 MiB/s 00:00 [####################################################] 100%
 python-defusedxml-0.6.0-4-any                                33.0 KiB  3.22 MiB/s 00:00 [####################################################] 100%
 python-prometheus_client-0.8.0-2-any                         81.3 KiB  3.97 MiB/s 00:00 [####################################################] 100%
 python-jinja-2.11.2-2-any                                   306.6 KiB  3.22 MiB/s 00:00 [####################################################] 100%
 python-tornado-6.1.0-1-x86_64                               639.7 KiB  3.47 MiB/s 00:00 [####################################################] 100%
 python-ptyprocess-0.6.0-4-any                                20.9 KiB  0.00   B/s 00:00 [####################################################] 100%
 python-terminado-0.9.1-1-any                                 22.7 KiB  7.40 MiB/s 00:00 [####################################################] 100%
 python-decorator-4.4.2-1-any                                 16.3 KiB  0.00   B/s 00:00 [####################################################] 100%
 python-traitlets-4.3.3-3-any                                158.6 KiB  3.10 MiB/s 00:00 [####################################################] 100%
 python-jupyter_core-4.6.3-2-any                              69.5 KiB  4.85 MiB/s 00:00 [####################################################] 100%
 python-zipp-3.4.0-1-any                                      10.4 KiB  0.00   B/s 00:00 [####################################################] 100%
 python-importlib-metadata-2.0.0-1-any                        48.0 KiB  4.69 MiB/s 00:00 [####################################################] 100%
 python-pyrsistent-0.17.3-1-x86_64                            91.5 KiB  2.98 MiB/s 00:00 [####################################################] 100%
 python-jsonschema-3.2.0-2-any                                99.9 KiB  2.44 MiB/s 00:00 [####################################################] 100%
 jupyter-nbformat-5.0.6-1-any                                131.2 KiB  4.74 MiB/s 00:00 [####################################################] 100%
 python-pexpect-4.8.0-1-any                                   76.1 KiB  10.6 MiB/s 00:00 [####################################################] 100%
 python-pickleshare-0.7.5-3-any                               10.8 KiB  0.00   B/s 00:00 [####################################################] 100%
 python-pygments-2.7.2-1-any                                1864.3 KiB  3.66 MiB/s 00:00 [####################################################] 100%
 python-wcwidth-0.2.5-1-any                                   32.2 KiB  10.5 MiB/s 00:00 [####################################################] 100%
 python-prompt_toolkit-3.0.8-1-any                           533.3 KiB  5.06 MiB/s 00:00 [####################################################] 100%
 python-parso-1:0.7.1-1-any                                  159.7 KiB  5.20 MiB/s 00:00 [####################################################] 100%
 python-jedi-0.17.2-1-any                                    969.6 KiB  3.30 MiB/s 00:00 [####################################################] 100%
 python-backcall-0.2.0-1-any                                  19.6 KiB  1397 KiB/s 00:00 [####################################################] 100%
 ipython-7.19.0-1-any                                       1063.9 KiB  1258 KiB/s 00:01 [####################################################] 100%
 python-ipykernel-5.3.4-1-any                                188.1 KiB  2.04 MiB/s 00:00 [####################################################] 100%
 python-pyzmq-19.0.1-2-x86_64                                431.2 KiB  3.32 MiB/s 00:00 [####################################################] 100%
 python-dateutil-2.8.1-3-any                                 270.7 KiB  4.72 MiB/s 00:00 [####################################################] 100%
 python-jupyter_client-6.1.7-1-any                           157.3 KiB  5.12 MiB/s 00:00 [####################################################] 100%
 mathjax2-2.7.9-1-any                                          6.0 MiB  2.52 MiB/s 00:02 [####################################################] 100%
 python-send2trash-1.5.0-4-any                                15.3 KiB  0.00   B/s 00:00 [####################################################] 100%
 python-mistune-0.8.4-3-any                                   24.4 KiB  0.00   B/s 00:00 [####################################################] 100%
 jupyter-widgetsnbextension-1:3.5.1-1-any                    826.7 KiB  3.56 MiB/s 00:00 [####################################################] 100%
 python-ipywidgets-7.5.1-4-any                               157.8 KiB  4.67 MiB/s 00:00 [####################################################] 100%
 jupyter_console-6.2.0-1-any                                  38.8 KiB  6.31 MiB/s 00:00 [####################################################] 100%
 jupyter-4.6.3-1-any                                           2.6 KiB  0.00   B/s 00:00 [####################################################] 100%
 python-entrypoints-0.3-3-any                                  6.4 KiB  0.00   B/s 00:00 [####################################################] 100%
 python-pandocfilters-1.4.3-1-any                             11.1 KiB  0.00   B/s 00:00 [####################################################] 100%
 python-bleach-3.2.1-1-any                                   238.0 KiB  3.52 MiB/s 00:00 [####################################################] 100%
 python-testpath-0.4.4-1-any                                   9.6 KiB  0.00   B/s 00:00 [####################################################] 100%
 jupyter-nbconvert-5.6.1-1-any                               439.9 KiB  3.14 MiB/s 00:00 [####################################################] 100%
 python-argon2_cffi-20.1.0-1-x86_64                           29.9 KiB  0.00   B/s 00:00 [####################################################] 100%
 jupyter-notebook-6.1.4-1-any                                  2.3 MiB  3.59 MiB/s 00:01 [####################################################] 100%
(43/43) 正在检查密钥环里的密钥                                                           [####################################################] 100%
(43/43) 正在检查软件包完整性                                                             [####################################################] 100%
(43/43) 正在加载软件包文件                                                               [####################################################] 100%
(43/43) 正在检查文件冲突                                                                 [####################################################] 100%
(43/43) 正在检查可用存储空间                                                             [####################################################] 100%
:: 正在处理软件包的变化...
( 1/43) 正在安装 python-markupsafe                                                       [####################################################] 100%
( 2/43) 正在安装 python-jinja                                                            [####################################################] 100%
python-jinja 的可选依赖
    python-babel: for i18n support
( 3/43) 正在安装 python-tornado                                                          [####################################################] 100%
python-tornado 的可选依赖
    python-pycurl: for tornado.curl_httpclient [已安装]
    python-twisted: for tornado.platform.twisted
( 4/43) 正在安装 python-ptyprocess                                                       [####################################################] 100%
( 5/43) 正在安装 python-terminado                                                        [####################################################] 100%
( 6/43) 正在安装 python-decorator                                                        [####################################################] 100%
( 7/43) 正在安装 python-traitlets                                                        [####################################################] 100%
( 8/43) 正在安装 python-jupyter_core                                                     [####################################################] 100%
( 9/43) 正在安装 python-attrs                                                            [####################################################] 100%
(10/43) 正在安装 python-zipp                                                             [####################################################] 100%
(11/43) 正在安装 python-importlib-metadata                                               [####################################################] 100%
(12/43) 正在安装 python-pyrsistent                                                       [####################################################] 100%
(13/43) 正在安装 python-jsonschema                                                       [####################################################] 100%
(14/43) 正在安装 jupyter-nbformat                                                        [####################################################] 100%
(15/43) 正在安装 python-pexpect                                                          [####################################################] 100%
(16/43) 正在安装 python-pickleshare                                                      [####################################################] 100%
(17/43) 正在安装 python-pygments                                                         [####################################################] 100%
(18/43) 正在安装 python-wcwidth                                                          [####################################################] 100%
(19/43) 正在安装 python-prompt_toolkit                                                   [####################################################] 100%
(20/43) 正在安装 python-parso                                                            [####################################################] 100%
(21/43) 正在安装 python-jedi                                                             [####################################################] 100%
(22/43) 正在安装 python-backcall                                                         [####################################################] 100%
(23/43) 正在安装 ipython                                                                 [####################################################] 100%
ipython 的可选依赖
    python-nose: for IPython's test suite
(24/43) 正在安装 python-ipykernel                                                        [####################################################] 100%
(25/43) 正在安装 python-pyzmq                                                            [####################################################] 100%
(26/43) 正在安装 python-dateutil                                                         [####################################################] 100%
(27/43) 正在安装 python-jupyter_client                                                   [####################################################] 100%
(28/43) 正在安装 mathjax2                                                                [####################################################] 100%
(29/43) 正在安装 python-send2trash                                                       [####################################################] 100%
(30/43) 正在安装 python-mistune                                                          [####################################################] 100%
(31/43) 正在安装 jupyter-widgetsnbextension                                              [####################################################] 100%
(32/43) 正在安装 python-ipywidgets                                                       [####################################################] 100%
(33/43) 正在安装 jupyter_console                                                         [####################################################] 100%
(34/43) 正在安装 jupyter                                                                 [####################################################] 100%
jupyter 的可选依赖
    jupyter-nbconvert: notebook conversion [等待中]
(35/43) 正在安装 python-entrypoints                                                      [####################################################] 100%
(36/43) 正在安装 python-pandocfilters                                                    [####################################################] 100%
(37/43) 正在安装 python-bleach                                                           [####################################################] 100%
(38/43) 正在安装 python-testpath                                                         [####################################################] 100%
(39/43) 正在安装 python-defusedxml                                                       [####################################################] 100%
(40/43) 正在安装 jupyter-nbconvert                                                       [####################################################] 100%
jupyter-nbconvert 的可选依赖
    pandoc: non-html conversion output
(41/43) 正在安装 python-prometheus_client                                                [####################################################] 100%
(42/43) 正在安装 python-argon2_cffi                                                      [####################################################] 100%
(43/43) 正在安装 jupyter-notebook                                                        [####################################################] 100%
jupyter-notebook 的可选依赖
    pandoc: notebook export
:: 正在运行事务后钩子函数...
(1/3) Arming ConditionNeedsUpdate...
(2/3) Updating fontconfig cache...
(3/3) Updating the desktop file MIME type cache...
```
## 2. Running Jupyter Notebook

```bash
❯ jupyter notebook
[I 09:48:05.602 NotebookApp] Writing notebook server cookie secret to /home/cxy/.local/share/jupyter/runtime/notebook_cookie_secret
[I 09:48:07.862 NotebookApp] Serving notebooks from local directory: /home/cxy
[I 09:48:07.862 NotebookApp] Jupyter Notebook 6.1.4 is running at:
[I 09:48:07.862 NotebookApp] http://localhost:8888/?token=f00699d5cc5051ef7375f14957f0929ffd25435299336776
[I 09:48:07.862 NotebookApp]  or http://127.0.0.1:8888/?token=f00699d5cc5051ef7375f14957f0929ffd25435299336776
[I 09:48:07.862 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 09:48:07.946 NotebookApp] 
    
    To access the notebook, open this file in a browser:
        file:///home/cxy/.local/share/jupyter/runtime/nbserver-2440-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/?token=f00699d5cc5051ef7375f14957f0929ffd25435299336776
     or http://127.0.0.1:8888/?token=f00699d5cc5051ef7375f14957f0929ffd25435299336776

```
## 3. Quit Jupyter Notebook

```bash
Ctrl + c

^C[I 10:35:22.781 NotebookApp] interrupted
Serving notebooks from local directory: /home/cxy
1 active kernel
Jupyter Notebook 6.1.4 is running at:
http://localhost:8888/?token=2a11d9779a874941ce92a4928cfd671357ec2106a8bc6392
 or http://127.0.0.1:8888/?token=2a11d9779a874941ce92a4928cfd671357ec2106a8bc6392
Shutdown this notebook server (y/[n])? y
[C 10:35:26.754 NotebookApp] Shutdown confirmed
[I 10:35:26.755 NotebookApp] Shutting down 1 kernel
[I 10:35:27.159 NotebookApp] Kernel shutdown: ca4466b7-f118-4cd4-9078-6fc5d4320af6
[I 10:35:27.160 NotebookApp] Shutting down 0 terminals
[I 10:35:27.167 NotebookApp] KernelRestarter: restarting kernel (1/5), keep random ports
WARNING:root:kernel ca4466b7-f118-4cd4-9078-6fc5d4320af6 restarted
[IPKernelApp] WARNING | Parent appears to have exited, shutting down.
```
## 4. Generating configuration file 

```bash
❯ jupyter notebook --generate-config
Writing default config to: /home/cxy/.jupyter/jupyter_notebook_config.py

```
## 5. Installing themes

```bash
❯ pip install --user jupyterthemes
Looking in indexes: https://mirrors.aliyun.com/pypi/simple/
/usr/lib/python3.8/site-packages/urllib3/connectionpool.py:981: InsecureRequestWarning: Unverified HTTPS request is being made to host 'mirrors.aliyun.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
Collecting jupyterthemes
/usr/lib/python3.8/site-packages/urllib3/connectionpool.py:981: InsecureRequestWarning: Unverified HTTPS request is being made to host 'mirrors.aliyun.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
  Downloading https://mirrors.aliyun.com/pypi/packages/8a/08/9dee6dfd7f2aad6c30282d55c8f495b4dc1e4747b4e2bdbeb80572ddf312/jupyterthemes-0.20.0-py2.py3-none-any.whl (7.0 MB)
     |████████████████████████████████| 7.0 MB 1.8 MB/s 
Requirement already satisfied: matplotlib>=1.4.3 in ./.local/lib/python3.8/site-packages (from jupyterthemes) (3.3.3)
Requirement already satisfied: ipython>=5.4.1 in ./.local/lib/python3.8/site-packages (from jupyterthemes) (7.19.0)
Requirement already satisfied: jupyter-core in /usr/lib/python3.8/site-packages (from jupyterthemes) (4.6.3)
/usr/lib/python3.8/site-packages/urllib3/connectionpool.py:981: InsecureRequestWarning: Unverified HTTPS request is being made to host 'mirrors.aliyun.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
Collecting lesscpy>=0.11.2
/usr/lib/python3.8/site-packages/urllib3/connectionpool.py:981: InsecureRequestWarning: Unverified HTTPS request is being made to host 'mirrors.aliyun.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
  Downloading https://mirrors.aliyun.com/pypi/packages/f8/d2/665cda6614e3556eaeb7553a3a2963624c2e3bc9636777a1bb654b87b027/lesscpy-0.14.0-py2.py3-none-any.whl (46 kB)
     |████████████████████████████████| 46 kB 597 kB/s 
Requirement already satisfied: notebook>=5.6.0 in /usr/lib/python3.8/site-packages (from jupyterthemes) (6.1.4)
Requirement already satisfied: numpy>=1.15 in ./.local/lib/python3.8/site-packages (from matplotlib>=1.4.3->jupyterthemes) (1.19.4)
Requirement already satisfied: pillow>=6.2.0 in /usr/lib/python3.8/site-packages (from matplotlib>=1.4.3->jupyterthemes) (7.2.0)
Requirement already satisfied: python-dateutil>=2.1 in ./.local/lib/python3.8/site-packages (from matplotlib>=1.4.3->jupyterthemes) (2.8.1)
Requirement already satisfied: kiwisolver>=1.0.1 in ./.local/lib/python3.8/site-packages (from matplotlib>=1.4.3->jupyterthemes) (1.3.1)
Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 in /usr/lib/python3.8/site-packages (from matplotlib>=1.4.3->jupyterthemes) (2.4.7)
Requirement already satisfied: cycler>=0.10 in ./.local/lib/python3.8/site-packages (from matplotlib>=1.4.3->jupyterthemes) (0.10.0)
Requirement already satisfied: traitlets>=4.2 in ./.local/lib/python3.8/site-packages (from ipython>=5.4.1->jupyterthemes) (5.0.5)
Requirement already satisfied: pickleshare in ./.local/lib/python3.8/site-packages (from ipython>=5.4.1->jupyterthemes) (0.7.5)
Requirement already satisfied: backcall in ./.local/lib/python3.8/site-packages (from ipython>=5.4.1->jupyterthemes) (0.2.0)
Requirement already satisfied: pexpect>4.3; sys_platform != "win32" in ./.local/lib/python3.8/site-packages (from ipython>=5.4.1->jupyterthemes) (4.8.0)
Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in ./.local/lib/python3.8/site-packages (from ipython>=5.4.1->jupyterthemes) (3.0.8)
Requirement already satisfied: decorator in ./.local/lib/python3.8/site-packages (from ipython>=5.4.1->jupyterthemes) (4.4.2)
Requirement already satisfied: pygments in ./.local/lib/python3.8/site-packages (from ipython>=5.4.1->jupyterthemes) (2.7.2)
Requirement already satisfied: jedi>=0.10 in ./.local/lib/python3.8/site-packages (from ipython>=5.4.1->jupyterthemes) (0.17.2)
Requirement already satisfied: setuptools>=18.5 in /usr/lib/python3.8/site-packages (from ipython>=5.4.1->jupyterthemes) (50.3.2)
Requirement already satisfied: ply in /usr/lib/python3.8/site-packages (from lesscpy>=0.11.2->jupyterthemes) (3.11)
Requirement already satisfied: six in /usr/lib/python3.8/site-packages (from lesscpy>=0.11.2->jupyterthemes) (1.15.0)
Requirement already satisfied: jinja2 in /usr/lib/python3.8/site-packages (from notebook>=5.6.0->jupyterthemes) (2.11.2)
Requirement already satisfied: tornado>=5.0 in /usr/lib/python3.8/site-packages (from notebook>=5.6.0->jupyterthemes) (6.1)
Requirement already satisfied: pyzmq>=17 in /usr/lib/python3.8/site-packages (from notebook>=5.6.0->jupyterthemes) (19.0.1)
Requirement already satisfied: argon2-cffi in /usr/lib/python3.8/site-packages (from notebook>=5.6.0->jupyterthemes) (20.1.0)
Requirement already satisfied: ipython_genutils in ./.local/lib/python3.8/site-packages (from notebook>=5.6.0->jupyterthemes) (0.2.0)
Requirement already satisfied: jupyter_client>=5.3.4 in /usr/lib/python3.8/site-packages (from notebook>=5.6.0->jupyterthemes) (6.1.7)
Requirement already satisfied: nbformat in /usr/lib/python3.8/site-packages (from notebook>=5.6.0->jupyterthemes) (5.0.6)
Requirement already satisfied: nbconvert in /usr/lib/python3.8/site-packages (from notebook>=5.6.0->jupyterthemes) (5.6.1)
Requirement already satisfied: ipykernel in /usr/lib/python3.8/site-packages (from notebook>=5.6.0->jupyterthemes) (5.3.4)
Requirement already satisfied: Send2Trash in /usr/lib/python3.8/site-packages (from notebook>=5.6.0->jupyterthemes) (1.5.0)
Requirement already satisfied: terminado>=0.8.3 in /usr/lib/python3.8/site-packages (from notebook>=5.6.0->jupyterthemes) (0.9.1)
Requirement already satisfied: prometheus_client in /usr/lib/python3.8/site-packages (from notebook>=5.6.0->jupyterthemes) (0.8.0)
Requirement already satisfied: ptyprocess>=0.5 in ./.local/lib/python3.8/site-packages (from pexpect>4.3; sys_platform != "win32"->ipython>=5.4.1->jupyterthemes) (0.6.0)
Requirement already satisfied: wcwidth in ./.local/lib/python3.8/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=5.4.1->jupyterthemes) (0.2.5)
Requirement already satisfied: parso<0.8.0,>=0.7.0 in ./.local/lib/python3.8/site-packages (from jedi>=0.10->ipython>=5.4.1->jupyterthemes) (0.7.1)
Requirement already satisfied: MarkupSafe>=0.23 in /usr/lib/python3.8/site-packages (from jinja2->notebook>=5.6.0->jupyterthemes) (1.1.1)
Requirement already satisfied: cffi>=1.0.0 in /usr/lib/python3.8/site-packages (from argon2-cffi->notebook>=5.6.0->jupyterthemes) (1.14.3)
Requirement already satisfied: mistune<2,>=0.8.1 in /usr/lib/python3.8/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (0.8.4)
Requirement already satisfied: entrypoints>=0.2.2 in /usr/lib/python3.8/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (0.3)
Requirement already satisfied: bleach in /usr/lib/python3.8/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (3.2.1)
Requirement already satisfied: pandocfilters>=1.4.1 in /usr/lib/python3.8/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (1.4.3)
Requirement already satisfied: testpath in /usr/lib/python3.8/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (0.4.4)
Requirement already satisfied: defusedxml in /usr/lib/python3.8/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (0.6.0)
Requirement already satisfied: pycparser in /usr/lib/python3.8/site-packages (from cffi>=1.0.0->argon2-cffi->notebook>=5.6.0->jupyterthemes) (2.20)
Requirement already satisfied: packaging in /usr/lib/python3.8/site-packages (from bleach->nbconvert->notebook>=5.6.0->jupyterthemes) (20.4)
Requirement already satisfied: webencodings in /usr/lib/python3.8/site-packages (from bleach->nbconvert->notebook>=5.6.0->jupyterthemes) (0.5.1)
Installing collected packages: lesscpy, jupyterthemes
Successfully installed jupyterthemes-0.20.0 lesscpy-0.14.0

```
## 6. View themes available

```bash
❯ jt -l
Available Themes: 
   chesterish
   grade3
   gruvboxd
   gruvboxl
   monokai
   oceans16
   onedork
   solarizedd
   solarizedl
```
## 7. Using a themes

```bash
jt -t monokai
```

## 8. Setting password

```bash
jupyter notebook password
```
## 9. Installing NbExtensions configurator

```bash

❯ pip install jupyter_nbextensions_configurator jupyter_contrib_nbextensions
Defaulting to user installation because normal site-packages is not writeable
Looking in indexes: https://mirrors.aliyun.com/pypi/simple/
/usr/lib/python3.8/site-packages/urllib3/connectionpool.py:981: InsecureRequestWarning: Unverified HTTPS request is being made to host 'mirrors.aliyun.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
Collecting jupyter_nbextensions_configurator
/usr/lib/python3.8/site-packages/urllib3/connectionpool.py:981: InsecureRequestWarning: Unverified HTTPS request is being made to host 'mirrors.aliyun.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
  Downloading https://mirrors.aliyun.com/pypi/packages/51/a3/d72d5f2dc10c5ccf5a6f4c79f636bf071a5ce462dedd07af2f70384db6cb/jupyter_nbextensions_configurator-0.4.1.tar.gz (479 kB)
     |████████████████████████████████| 479 kB 1.5 MB/s 
/usr/lib/python3.8/site-packages/urllib3/connectionpool.py:981: InsecureRequestWarning: Unverified HTTPS request is being made to host 'mirrors.aliyun.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
Collecting jupyter_contrib_nbextensions
/usr/lib/python3.8/site-packages/urllib3/connectionpool.py:981: InsecureRequestWarning: Unverified HTTPS request is being made to host 'mirrors.aliyun.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
  Downloading https://mirrors.aliyun.com/pypi/packages/33/f0/6e2c00afda860f655fbf0f795f7310bdbf12122846344dfdc803fc7455d5/jupyter_contrib_nbextensions-0.5.1-py2.py3-none-any.whl (20.9 MB)
     |████████████████████████████████| 20.9 MB 134 kB/s 
/usr/lib/python3.8/site-packages/urllib3/connectionpool.py:981: InsecureRequestWarning: Unverified HTTPS request is being made to host 'mirrors.aliyun.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
Collecting jupyter_contrib_core>=0.3.3
/usr/lib/python3.8/site-packages/urllib3/connectionpool.py:981: InsecureRequestWarning: Unverified HTTPS request is being made to host 'mirrors.aliyun.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
  Downloading https://mirrors.aliyun.com/pypi/packages/e6/8f/04a752a8b66a66e7092c035e5d87d2502ac7ec07f9fb6059059b6c0dc272/jupyter_contrib_core-0.3.3-py2.py3-none-any.whl (18 kB)
Requirement already satisfied: jupyter_core in /usr/lib/python3.8/site-packages (from jupyter_nbextensions_configurator) (4.6.3)
Requirement already satisfied: notebook>=4.0 in /usr/lib/python3.8/site-packages (from jupyter_nbextensions_configurator) (6.1.4)
Requirement already satisfied: pyyaml in /usr/lib/python3.8/site-packages (from jupyter_nbextensions_configurator) (5.3.1)
Requirement already satisfied: tornado in /usr/lib/python3.8/site-packages (from jupyter_nbextensions_configurator) (6.1)
Requirement already satisfied: traitlets in ./.local/lib/python3.8/site-packages (from jupyter_nbextensions_configurator) (5.0.5)
Requirement already satisfied: ipython-genutils in ./.local/lib/python3.8/site-packages (from jupyter_contrib_nbextensions) (0.2.0)
Requirement already satisfied: lxml in ./.local/lib/python3.8/site-packages (from jupyter_contrib_nbextensions) (4.6.2)
Requirement already satisfied: nbconvert>=4.2 in /usr/lib/python3.8/site-packages (from jupyter_contrib_nbextensions) (5.6.1)
/usr/lib/python3.8/site-packages/urllib3/connectionpool.py:981: InsecureRequestWarning: Unverified HTTPS request is being made to host 'mirrors.aliyun.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
Collecting jupyter-highlight-selected-word>=0.1.1
/usr/lib/python3.8/site-packages/urllib3/connectionpool.py:981: InsecureRequestWarning: Unverified HTTPS request is being made to host 'mirrors.aliyun.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
  Downloading https://mirrors.aliyun.com/pypi/packages/50/d7/19ab7cfd60bf268d2abbacc52d4295a40f52d74dfc0d938e4761ee5e598b/jupyter_highlight_selected_word-0.2.0-py2.py3-none-any.whl (11 kB)
/usr/lib/python3.8/site-packages/urllib3/connectionpool.py:981: InsecureRequestWarning: Unverified HTTPS request is being made to host 'mirrors.aliyun.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
Collecting jupyter-latex-envs>=1.3.8
/usr/lib/python3.8/site-packages/urllib3/connectionpool.py:981: InsecureRequestWarning: Unverified HTTPS request is being made to host 'mirrors.aliyun.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
  Downloading https://mirrors.aliyun.com/pypi/packages/0e/15/55805de080d5542f76920364635e96e64d3b37f678befdfe3b16aa154205/jupyter_latex_envs-1.4.6.tar.gz (861 kB)
     |████████████████████████████████| 861 kB 1.5 MB/s 
Requirement already satisfied: setuptools in /usr/lib/python3.8/site-packages (from jupyter_contrib_core>=0.3.3->jupyter_nbextensions_configurator) (50.3.2)
Requirement already satisfied: jinja2 in /usr/lib/python3.8/site-packages (from notebook>=4.0->jupyter_nbextensions_configurator) (2.11.2)
Requirement already satisfied: pyzmq>=17 in /usr/lib/python3.8/site-packages (from notebook>=4.0->jupyter_nbextensions_configurator) (19.0.1)
Requirement already satisfied: argon2-cffi in /usr/lib/python3.8/site-packages (from notebook>=4.0->jupyter_nbextensions_configurator) (20.1.0)
Requirement already satisfied: jupyter_client>=5.3.4 in /usr/lib/python3.8/site-packages (from notebook>=4.0->jupyter_nbextensions_configurator) (6.1.7)
Requirement already satisfied: nbformat in /usr/lib/python3.8/site-packages (from notebook>=4.0->jupyter_nbextensions_configurator) (5.0.6)
Requirement already satisfied: ipykernel in /usr/lib/python3.8/site-packages (from notebook>=4.0->jupyter_nbextensions_configurator) (5.3.4)
Requirement already satisfied: Send2Trash in /usr/lib/python3.8/site-packages (from notebook>=4.0->jupyter_nbextensions_configurator) (1.5.0)
Requirement already satisfied: terminado>=0.8.3 in /usr/lib/python3.8/site-packages (from notebook>=4.0->jupyter_nbextensions_configurator) (0.9.1)
Requirement already satisfied: prometheus_client in /usr/lib/python3.8/site-packages (from notebook>=4.0->jupyter_nbextensions_configurator) (0.8.0)
Requirement already satisfied: mistune<2,>=0.8.1 in /usr/lib/python3.8/site-packages (from nbconvert>=4.2->jupyter_contrib_nbextensions) (0.8.4)
Requirement already satisfied: pygments in ./.local/lib/python3.8/site-packages (from nbconvert>=4.2->jupyter_contrib_nbextensions) (2.7.2)
Requirement already satisfied: entrypoints>=0.2.2 in /usr/lib/python3.8/site-packages (from nbconvert>=4.2->jupyter_contrib_nbextensions) (0.3)
Requirement already satisfied: bleach in /usr/lib/python3.8/site-packages (from nbconvert>=4.2->jupyter_contrib_nbextensions) (3.2.1)
Requirement already satisfied: pandocfilters>=1.4.1 in /usr/lib/python3.8/site-packages (from nbconvert>=4.2->jupyter_contrib_nbextensions) (1.4.3)
Requirement already satisfied: testpath in /usr/lib/python3.8/site-packages (from nbconvert>=4.2->jupyter_contrib_nbextensions) (0.4.4)
Requirement already satisfied: defusedxml in /usr/lib/python3.8/site-packages (from nbconvert>=4.2->jupyter_contrib_nbextensions) (0.6.0)
Requirement already satisfied: ipython in ./.local/lib/python3.8/site-packages (from jupyter-latex-envs>=1.3.8->jupyter_contrib_nbextensions) (7.19.0)
Requirement already satisfied: MarkupSafe>=0.23 in /usr/lib/python3.8/site-packages (from jinja2->notebook>=4.0->jupyter_nbextensions_configurator) (1.1.1)
Requirement already satisfied: cffi>=1.0.0 in /usr/lib/python3.8/site-packages (from argon2-cffi->notebook>=4.0->jupyter_nbextensions_configurator) (1.14.3)
Requirement already satisfied: six in /usr/lib/python3.8/site-packages (from argon2-cffi->notebook>=4.0->jupyter_nbextensions_configurator) (1.15.0)
Requirement already satisfied: python-dateutil>=2.1 in ./.local/lib/python3.8/site-packages (from jupyter_client>=5.3.4->notebook>=4.0->jupyter_nbextensions_configurator) (2.8.1)
Requirement already satisfied: ptyprocess in ./.local/lib/python3.8/site-packages (from terminado>=0.8.3->notebook>=4.0->jupyter_nbextensions_configurator) (0.6.0)
Requirement already satisfied: packaging in /usr/lib/python3.8/site-packages (from bleach->nbconvert>=4.2->jupyter_contrib_nbextensions) (20.4)
Requirement already satisfied: webencodings in /usr/lib/python3.8/site-packages (from bleach->nbconvert>=4.2->jupyter_contrib_nbextensions) (0.5.1)
Requirement already satisfied: pexpect>4.3; sys_platform != "win32" in ./.local/lib/python3.8/site-packages (from ipython->jupyter-latex-envs>=1.3.8->jupyter_contrib_nbextensions) (4.8.0)
Requirement already satisfied: pickleshare in ./.local/lib/python3.8/site-packages (from ipython->jupyter-latex-envs>=1.3.8->jupyter_contrib_nbextensions) (0.7.5)
Requirement already satisfied: jedi>=0.10 in ./.local/lib/python3.8/site-packages (from ipython->jupyter-latex-envs>=1.3.8->jupyter_contrib_nbextensions) (0.17.2)
Requirement already satisfied: decorator in ./.local/lib/python3.8/site-packages (from ipython->jupyter-latex-envs>=1.3.8->jupyter_contrib_nbextensions) (4.4.2)
Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in ./.local/lib/python3.8/site-packages (from ipython->jupyter-latex-envs>=1.3.8->jupyter_contrib_nbextensions) (3.0.8)
Requirement already satisfied: backcall in ./.local/lib/python3.8/site-packages (from ipython->jupyter-latex-envs>=1.3.8->jupyter_contrib_nbextensions) (0.2.0)
Requirement already satisfied: pycparser in /usr/lib/python3.8/site-packages (from cffi>=1.0.0->argon2-cffi->notebook>=4.0->jupyter_nbextensions_configurator) (2.20)
Requirement already satisfied: pyparsing>=2.0.2 in /usr/lib/python3.8/site-packages (from packaging->bleach->nbconvert>=4.2->jupyter_contrib_nbextensions) (2.4.7)
Requirement already satisfied: parso<0.8.0,>=0.7.0 in ./.local/lib/python3.8/site-packages (from jedi>=0.10->ipython->jupyter-latex-envs>=1.3.8->jupyter_contrib_nbextensions) (0.7.1)
Requirement already satisfied: wcwidth in ./.local/lib/python3.8/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython->jupyter-latex-envs>=1.3.8->jupyter_contrib_nbextensions) (0.2.5)
Using legacy 'setup.py install' for jupyter-nbextensions-configurator, since package 'wheel' is not installed.
Using legacy 'setup.py install' for jupyter-latex-envs, since package 'wheel' is not installed.
Installing collected packages: jupyter-contrib-core, jupyter-nbextensions-configurator, jupyter-highlight-selected-word, jupyter-latex-envs, jupyter-contrib-nbextensions
    Running setup.py install for jupyter-nbextensions-configurator ... done
    Running setup.py install for jupyter-latex-envs ... done
Successfully installed jupyter-contrib-core-0.3.3 jupyter-contrib-nbextensions-0.5.1 jupyter-highlight-selected-word-0.2.0 jupyter-latex-envs-1.4.6 jupyter-nbextensions-configurator-0.4.1

❯ jupyter contrib nbextension install --user


❯ jupyter nbextensions_configurator enable --user
Enabling: jupyter_nbextensions_configurator
- Writing config: /home/cxy/.jupyter
    - Validating...
      jupyter_nbextensions_configurator 0.4.1 OK
Enabling notebook nbextension nbextensions_configurator/config_menu/main...
```


