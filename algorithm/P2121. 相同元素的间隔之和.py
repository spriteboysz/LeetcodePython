#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-25 23:21:59
LastEditTime: 2022-02-25 23:27:52
Description: 
FilePath: 2121.相同元素的间隔之和.py
"""
#
# @lc app=leetcode.cn id=2121 lang=python3
#
# [2121] 相同元素的间隔之和
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        distances = [0] * len(arr)
        numindex = defaultdict(list)
        for i, num in enumerate(arr):
            numindex[num].append(i)
        print(numindex)
        for i, num in enumerate(arr):
            distances[i] = sum(map(lambda el: abs(el - i), numindex[num]))
        return distances


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.getDistances([2, 1, 3, 1, 2, 3, 3])
    print(ans)
    ans = solution.getDistances([10, 5, 10, 10])
    print(ans)
