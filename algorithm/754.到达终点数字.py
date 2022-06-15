#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-15 23:04
LastEditTime: 2022-06-15 23:04
Description:
FilePath: 754.到达终点数字.py
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        if target < 0:
            target = -target
        i = 1
        while True:
            s = (i * i + i) // 2
            if s >= target and (s - target) % 2 == 0:
                return i
            i += 1


if __name__ == '__main__':
    solution = Solution()
    ans = solution.reachNumber(2)
    print(ans)
