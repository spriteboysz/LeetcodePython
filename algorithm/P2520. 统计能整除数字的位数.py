#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/25 11:52
FileName: algorithm/P2520. 统计能整除数字的位数.py
Description: 
"""


class Solution:
    def countDigits(self, num: int) -> int:
        cnt = 0
        for c in str(num):
            if num % int(c) == 0:
                cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().countDigits(121))
