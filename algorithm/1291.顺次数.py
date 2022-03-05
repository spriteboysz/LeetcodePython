#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-05 16:10:36
LastEditTime: 2022-03-05 16:29:38
Description: 
FilePath: 1291.顺次数.py
"""
#
# @lc app=leetcode.cn id=1291 lang=python3
#
# [1291] 顺次数
#

# @lc code=start
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        base = [i for i in range(1, 10)]
        minimum, maximum = len(str(low)), len(str(high))
        sequential = []
        for k in range(minimum, maximum + 1):
            for i in range(10 - k):
                num = 0
                for j in range(k):
                    num += base[i + j] * 10 ** (k - j - 1)
                if low <= num <= high:
                    sequential.append(num)
        return sequential


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.sequentialDigits(100, 300)
    print(ans)
    ans = solution.sequentialDigits(1000, 13000)
    print(ans)
