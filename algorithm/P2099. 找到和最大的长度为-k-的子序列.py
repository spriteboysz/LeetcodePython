#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-21 22:28:06
LastEditTime: 2022-01-21 22:46:24
Description:
FilePath: 2099.找到和最大的长度为-k-的子序列.py
"""
#
# @lc app=leetcode.cn id=2099 lang=python3
#
# [2099] 找到和最大的长度为 K 的子序列
#

# @lc code=start
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sequence = list(sorted(nums, reverse=True))[:k]
        subsequence = []
        for num in nums:
            if num in sequence:
                subsequence.append(num)
                sequence.remove(num)
        return subsequence

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubsequence([3, 4, 3, 3], 2))
