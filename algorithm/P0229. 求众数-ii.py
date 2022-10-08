#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-10 22:27:02
LastEditTime: 2022-02-10 22:32:06
Description: 
FilePath: 229.求众数-ii.py
'''
#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#

# @lc code=start
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = dict()
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        majority = []
        for k, v in count.items():
            if v > len(nums) // 3:
                majority.append(k)
        return majority
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([1]))
    print(s.majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))
