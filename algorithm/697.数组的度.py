#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-21 23:16:19
LastEditTime: 2022-02-21 23:20:44
Description: 
FilePath: 697.数组的度.py
"""
#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = dict()
        for i, num in enumerate(nums):
            if num not in counts:
                counts[num] = [1, i, i]
            else:
                counts[num][0] += 1
                counts[num][2] = i
        degree = max(
            list(counts.items()), key=lambda el: (el[1][0], el[1][1] - el[1][2])
        )
        return degree[1][2] - degree[1][1] + 1


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findShortestSubArray([1, 2, 2, 3, 1])
    print(ans)
    ans2 = solution.findShortestSubArray([1, 2, 2, 3, 1, 4, 2])
    print(ans2)
