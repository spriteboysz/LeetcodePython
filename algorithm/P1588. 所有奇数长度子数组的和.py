#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-29 22:15:22
LastEditTime: 2022-01-29 22:22:05
Description:
FilePath: 1588.所有奇数长度子数组的和.py
"""
#
# @lc app=leetcode.cn id=1588 lang=python3
#
# [1588] 所有奇数长度子数组的和
#

# @lc code=start
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1, 2):
                count += sum(arr[i:j])
        return count
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
    print(s.sumOddLengthSubarrays([1, 2]))
    print(s.sumOddLengthSubarrays([10, 11, 12]))
