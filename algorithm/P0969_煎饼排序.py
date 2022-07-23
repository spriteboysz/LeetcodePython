#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-27 21:35:16
LastEditTime: 2022-04-27 21:39:53
Description: 
FilePath: 969.煎饼排序.py
"""
#
# @lc app=leetcode.cn id=969 lang=python3
#
# [969] 煎饼排序
#

# @lc code=start
from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        pancake = []
        for _ in range(len(arr)):
            index = arr.index(max(arr)) + 1
            pancake.append(index)
            pancake.append(len(arr))
            arr = (arr[:index][::-1] + arr[index:])[::-1][:-1]
        return pancake


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.pancakeSort([3, 2, 4, 1])
    print(ans)
    ans = solution.pancakeSort([1, 2, 3])
    print(ans)
