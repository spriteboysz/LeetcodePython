#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-16 00:07:56
LastEditTime: 2022-02-16 00:21:47
Description: 
FilePath: 1.两数之和.py
'''
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
