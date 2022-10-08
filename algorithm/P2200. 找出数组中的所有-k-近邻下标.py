#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-30 22:16:07
LastEditTime: 2022-03-30 22:19:25
Description: 
FilePath: 2200.找出数组中的所有-k-近邻下标.py
"""
#
# @lc app=leetcode.cn id=2200 lang=python3
#
# [2200] 找出数组中的所有 K 近邻下标
#

# @lc code=start
from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indices = []
        for i, num in enumerate(nums):
            if num == key:
                indices.extend(range(i - k, i + k + 1))
        return sorted(list(set(indices) & set(range(len(nums)))))


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findKDistantIndices(nums=[3, 4, 9, 1, 3, 9, 5], key=9, k=1)
    print(ans)

    ans = solution.findKDistantIndices(nums=[2, 2, 2, 2, 2], key=2, k=2)
    print(ans)
