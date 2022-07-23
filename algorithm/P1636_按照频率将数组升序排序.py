#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-27 22:42:42
LastEditTime: 2022-01-27 22:44:57
Description: 
FilePath: 1636.按照频率将数组升序排序.py
'''
#
# @lc app=leetcode.cn id=1636 lang=python3
#
# [1636] 按照频率将数组升序排序
#

# @lc code=start
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return list(sorted(nums, key=lambda el: (nums.count(el), -el)))
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.frequencySort([2, 3, 1, 3, 2]))
