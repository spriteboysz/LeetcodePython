#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-21 22:50:47
LastEditTime: 2022-01-21 22:56:40
Description: 
FilePath: 2094.找出-3-位偶数.py
'''
#
# @lc app=leetcode.cn id=2094 lang=python3
#
# [2094] 找出 3 位偶数
#

# @lc code=start
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        even = set()
        for i in range(len(digits)):
            if digits[i] == 0:
                continue
            for j in range(len(digits)):
                if i == j:
                    continue
                for k in range(len(digits)):
                    if i == k or j == k or digits[k] % 2:
                        continue
                    even.add(digits[i] * 100 + digits[j] * 10 + digits[k])
        return list(sorted(even))
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.findEvenNumbers([2, 2, 8, 8, 2]))
