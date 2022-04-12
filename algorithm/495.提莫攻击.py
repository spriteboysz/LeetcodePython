#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-11 23:03:10
LastEditTime: 2022-04-11 23:06:53
Description: 
FilePath: 495.提莫攻击.py
"""
#
# @lc app=leetcode.cn id=495 lang=python3
#
# [495] 提莫攻击
#

# @lc code=start
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count = duration
        for i in range(1, len(timeSeries)):
            count += min(duration, timeSeries[i] - timeSeries[i - 1])

        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findPoisonedDuration([1, 4], 2)
    print(ans)
    ans = solution.findPoisonedDuration([1, 2], 2)
    print(ans)
