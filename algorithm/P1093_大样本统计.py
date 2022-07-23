#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-05 22:30:08
LastEditTime: 2022-03-05 22:39:19
Description: 
FilePath: 1093.大样本统计.py
"""
#
# @lc app=leetcode.cn id=1093 lang=python3
#
# [1093] 大样本统计
#

# @lc code=start
from typing import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n = sum(count)
        minimum, maximum, mean, median, mode = 256, 0, 0, 0, 0
        total = 0
        for i, amount in enumerate(count):
            total += i * amount
            if minimum == 256 and amount != 0:
                minimum = i
            if amount != 0:
                maximum = i
        mean = total / n
        mode = count.index(max(count))
        s = 256
        if n % 2 == 1:
            n = int(n / 2)
            for i, amount in enumerate(count):
                n -= amount
                if n < 0:
                    median = i
                    break
        else:
            n1, n2 = int(n / 2) - 1, int(n / 2)
            for i, amount in enumerate(count):
                n1 -= amount
                n2 -= amount
                if n1 < 0:
                    s = min(s, i)
                if n2 < 0:
                    s += i
                    median = s / 2
                    break

        return [minimum, maximum, mean, median, mode]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.sampleStats(
        count=[
            0,
            4,
            3,
            2,
            2,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ]
    )
    print(ans)
