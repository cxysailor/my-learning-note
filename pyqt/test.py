#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : test.py
#   Last Modified : 2021-01-04 18:48
#   Describe      :
#
# ====================================================

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout

class WidgetDemo(QWidget):
    """docstring for WidgetDemo"""
    def __init__(self):
        super().__init__()
        self.btn = QPushButton('Ok')
        self.btn1 = QPushButton('Cancel')
        self.init_ui()

    def init_ui(self):
        """Initializing of Widget"""
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.btn)
        hlayout.addWidget(self.btn1)
        self.setLayout(hlayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = WidgetDemo()
    demo.show()
    sys.exit(app.exec_())
