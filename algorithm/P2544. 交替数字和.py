#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/28 23:23
FileName: algorithm/P2544. 交替数字和.py
Description: 
"""


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        flag, sum = 1, 0
        for item in str(n):
            value = int(item) * flag
            flag = flag * -1
            sum += value
        return sum


if __name__ == '__main__':
    print(Solution().alternateDigitSum(521))
    print(Solution().alternateDigitSum(111))
    print(Solution().alternateDigitSum(886996))
