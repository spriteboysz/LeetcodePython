#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-05 16:01:58
Description: 
FilePath: 412.fizz-buzz.py
'''
#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                lst.append("FizzBuzz")
            elif i % 3 == 0:
                lst.append("Fizz")
            elif i % 5 == 0:
                lst.append("Buzz")
            else:
                lst.append(str(i))

        return lst
# @lc code=end

