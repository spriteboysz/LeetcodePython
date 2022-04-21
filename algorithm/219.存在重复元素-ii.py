#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-07 22:26:11
LastEditTime: 2022-04-21 22:47:33
Description: 
FilePath: 219.存在重复元素-ii.py
"""
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
        s = set()
        for i in range(len(nums)):
            if i > k:
                s.remove(nums[i - k - 1])
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(s.containsNearbyDuplicate([1, 0, 1, 1], 1))
    print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
