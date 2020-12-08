# 数据分析numpy、matplotlib、pandas

## 1. 简述数据分析

### 1. 数据分析简介

- 数据分析指用适当的统计、分析方法对收集来的大量数据进行分析，将它们加以汇总和理解并消化，以求最大化地开发数据的功能，发挥数据的作用。数据分析是为了提取有用信息和形成结论而对数据加以详细研究和概括总结的过程
- 数据也称为观测值，是实验、测量、观察、调查等的结果。数据分析中所处理的数据分为定性数据和定量数据。只能归入某一类而不能用数值进行测度的数据称为定性数据。定性数据中表现为类别，但不区分顺序的，是定类数据，如性别、品牌等；定性数据中表现为类别，但区分顺序的，是定序数据，如学历、商品的质量等级等

### 2. 数据分析到目的

- 数据分析的目的是把隐藏在一大批看来杂乱无章的数据中的信息集中和提炼出来，从而找出所研究对象的内在规律。在实际应用中，数据分析可帮助人们做出判断，以便采取适当行动。数据分析是有组织有目的地收集数据、分析数据，使之成为信息的过程。这一过程是质量管理体系的支持过程。在产品的整个寿命周期，包括从市场调研到售后服务和最终处置的各个过程都需要适当运用数据分析过程，以提升有效性。例如设计人员在开始一个新的设计以前，要通过广泛的设计调查，分析所得数据以判定设计方向，因此数据分析在工业设计中具有极其重要的地位
- 数据分析是Python数据科学的基础
- 数据分析是机器学习的基础

## Matplotlib基本操作

### 1. 安装

```bash
pip install --user matplotlib
```

### 2. 导入包

```python
from matplotlib import pyplot as plt
```

### 3. 基本流程

```python
from matplotlib import pyplot as plt

x = range(2, 26, 2)  # x轴的数据 - 可迭代对象
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]  # y轴的数据 - 可迭代对象
# x轴和y轴的数据一起组成了要绘制的坐标,即(2,15)(4,13)(6,14.5)...这样的坐标点
# 绘制折线图
plt.plot(x, y)
# 程序执行时展示图形
plt.show()
```
生成的折线图图形是这样的:

![折线图Figure_1.png](./Figure_1.png) 

### 4. Figure

可以使用figure()方法画多个图形

```python
from matplotlib import pyplot as plt
import numpy as np


class MatplotlibFigure(object):
    """Matplotlib的figure方法"""
    def __init__(self):
        super(MatplotlibFigure, self).__init__()
        # x轴的数据
        self.x = np.linspace(-1, 1, 50)
        # y轴的数据
        self.y1 = self.x * 2 + 1
        self.y2 = self.x ** 2

    def generate_figure(self):
        """生成图形"""
        # 第一个图形 - 以y1为y轴数据
        plt.figure()
        plt.plot(self.x, self.y1)
        # 第二个图形 - 以y2为y轴数据
        plt.figure(num=5)
        plt.plot(self.x, self.y1)
        # 设置一些属性 - 颜色、线条宽度、线条样式
        plt.plot(self.x, self.y2, color='red', linewidth=5, linestyle='dashdot')
        plt.show()


if __name__ == "__main__":
    mf = MatplotlibFigure()
    mf.generate_figure()
```

### 5. 设置坐标轴

```python
from matplotlib import pyplot as plt
import numpy as np


class AxesSetting(object):
    """设置坐标轴"""
    def __init__(self):
        super(AxesSetting, self).__init__()
        # x轴的数据
        self.x = np.linspace(-3, 3, 50)
        # y轴的数据
        self.y1 = self.x * 2 + 1
        self.y2 = self.x ** 2
        # 坐标轴的刻度
        self.new_ticks = np.linspace(-1, 2, 5)

    def generate_figure(self):
        """生成图形"""
        plt.figure()
        plt.plot(self.x, self.y1, color='red', linewidth=1.0, linestyle='--')
        plt.plot(self.x, self.y2)

        # 设置数据区间
        plt.xlim((-1, 2))
        plt.ylim((-2, 3))
        # 设置坐标轴标签
        plt.xlabel('I am x')
        plt.ylabel('I am y')

        # 设置坐标轴刻度
        plt.xticks(self.new_ticks)
        # 同时对y轴的刻度字体进行了一些修饰 - 支持正则与Latex
        plt.yticks([-2, -1.8, -1, 1.22, 3],
                [r'$really\ bad$', '$bad$', '$normal$', '$good$', r'$really\ good$'])

        # 显示图形
        plt.show()


if __name__ == "__main__":
    st = AxesSetting()
    st.generate_figure()
```
![Figure_2.png](./Figure_2.png) 

```python
from matplotlib import pyplot as plt
import numpy as np


class SettingAxes(object):
    """docstring for SettingAxes"""
    def __init__(self):
        super(SettingAxes, self).__init__()
        self.x = np.linspace(-3, 3, 50)
        self.y1 = self.x * 2 + 1
        self.y2 = self.x ** 2
        self.new_ticks = np.linspace(-1, 2, 5)

    def generate_figure(self):
        plt.figure()
        plt.plot(self.x, self.y1)
        plt.plot(self.x, self.y2, color='green', linewidth=1.0, linestyle='--')

        # 设置数据区间
        plt.xlim((-1, 2))
        plt.ylim((-2, 3))
        # 设置坐标轴标签
        plt.xlabel('I am x')
        plt.ylabel('I am y')

        # 设置坐标轴刻度
        plt.xticks(self.new_ticks)
        plt.yticks([-2, -1.8, -1, 1.22, 3],
                [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

        # 获取坐标轴 gca - get current axis
        ax = plt.gca()
        # 设置图片边框线颜色
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        # 设置坐标原点
        ax.xaxis.set_ticks_position('bottom')  # x轴刻度在底部
        ax.yaxis.set_ticks_position('left')  # y轴刻度在左侧
        # 设置坐标原点到(0,0)点处
        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['left'].set_position(('data', 0))

        plt.show()


if __name__ == "__main__":
    sa = SettingAxes()
    sa.generate_figure()
```
![Figure_3](./Figure_3.png) 

### 6. 图例legend

```python
from matplotlib import pyplot as plt
import numpy as np


class LengendSetting(object):
    """docstring for LengendSetting"""
    def __init__(self):
        super(LengendSetting, self).__init__()
        self.x = np.linspace(-3, 3, 50)
        self.y1 = self.x * 2 + 1
        self.y2 = self.x ** 2
        self.new_ticks = np.linspace(-1, 2, 5)

    def generate_figure(self):
        plt.figure()
        plt.xlim((-1, 2))
        plt.ylim((-2, 3))
        plt.xlabel('I am x')
        plt.ylabel('I am y')
        plt.xticks(self.new_ticks)
        plt.yticks([-2, -1.8, -1, 1.22, 3],
                [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
        # 要加上一个逗号
        l1, = plt.plot(self.x, self.y2, color='red', linestyle='--', label='Up')
        l2, = plt.plot(self.x, self.y1, label='Down')

        # 使用labels参数就不再使用上面设置的label了
        plt.legend(handles=[l1, l2], labels=['Conic', 'Straight line'], loc='best')

        plt.show()


if __name__ == "__main__":
    ls = LengendSetting()
    ls.generate_figure()
```
![Figure_4](./Figure_4.png)

### 7. 标注annotation

