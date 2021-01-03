#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : divisible.py
#   Last Modified : 2020-12-21 23:24
#   Describe      : 
#
# ====================================================


class IsDivisible(object):
    """Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero digits.

Examples: 1) n = 3, x = 1, y = 3 => true because 3 is divisible by 1 and 3 2) n = 12, x = 2, y = 6 => true because 12 is divisible by 2 and 6 3) n = 100, x = 5, y = 3 => false because 100 is not divisible by 3 4) n = 12, x = 7, y = 5 => false because 12 is neither divisible by 7 nor 5"""
    def __init__(self, num, x, y):
        super(IsDivisible, self).__init__()
        self.num = num
        self.x = x
        self.y = y
        
    def determine(self):
        """判断是否能整除"""
        if not self.num % self.x and not self.num % self.y:
            print(f'{self.num} is divisible by {self.x} and {self.y}')
        else:
            print(f'{self.num} is not divisible by {self.x} and {self.y}')



if __name__ == "__main__":
    n1 = int(input('Please enter an integer:'))
    n2 = int(input('Please enter second integer:'))
    n3 = int(input('Please enter third integer:'))
    id = IsDivisible(n1, n2, n3)
    id.determine()
