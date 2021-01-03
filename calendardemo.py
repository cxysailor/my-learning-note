#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : calendardemo.py
#   Last Modified : 2020-12-30 11:56
#   Describe      : 
#
# ====================================================

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class CalendarDemo(QWidget):
    """docstring for CalendarDemo"""
    def __init__(self):
        super(CalendarDemo, self).__init__()
        self.cal = QCalendarWidget(self)
        self.lbl = QLabel(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Calendar')
        self.resize(300, 300)
        self.cal.setMinimumDate(QDate(1988, 1, 1))
        self.cal.setMaximumDate(QDate(2088, 1, 1))
        self.cal.setGridVisible(True)
        self.cal.move(20, 20)
        date = self.cal.selectedDate()
        self.cal.clicked.connect(self.show_date)
        self.lbl.setText(date.toString('yyyy-MM-dd dddd'))
        self.lbl.move(20, 250)

    def show_date(self, date):
        self.lbl.setText((date.toString('yyyy-MM-dd dddd')))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CalendarDemo()
    sys.exit(app.exec_())
