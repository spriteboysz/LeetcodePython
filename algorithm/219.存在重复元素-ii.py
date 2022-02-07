#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-07 22:26:11
LastEditTime: 2022-02-07 22:52:17
Description: 
FilePath: 219.存在重复元素-ii.py
'''
#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
# no submit!
# @lc code=start
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(0, len(nums)-1):
            if nums[i] in nums[i + 1: i + 1 + k]:
                return True
        return False
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1, 2, 3, 1], 2))
    print(s.containsNearbyDuplicate([1, 0, 1, 0], 1))
    print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
