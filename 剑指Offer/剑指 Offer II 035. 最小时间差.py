#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-16 23:39:27
LastEditTime: 2022-05-16 23:42:01
Description: 
FilePath: 剑指 Offer II 035. 最小时间差.py
"""

from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 24 * 60:
            return 0
        minutes = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        minutes.append(minutes[0] + 24 * 60)

        return min(minutes[i] - minutes[i - 1] for i in range(1, len(minutes)))


if __name__ == "__main__":
    solution = Solution()
    ans = solution.findMinDifference(timePoints=["23:59", "00:00"])
    print(ans)
