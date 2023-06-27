#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-12 23:10:27
LastEditTime: 2022-04-12 23:12:46
Description: 
FilePath: 2215.找出两数组的不同.py
"""
#
# @lc app=leetcode.cn id=2215 lang=python3
#
# [2215] 找出两数组的不同
#

# @lc code=start
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [
            [num for num in set(nums1) if num not in nums2],
            [num for num in set(nums2) if num not in nums1],
        ]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findDifference([1, 2, 3], [2, 4, 6])
    print(ans)
    ans = solution.findDifference([1, 2, 3, 3], [1, 1, 2, 2])
    print(ans)
