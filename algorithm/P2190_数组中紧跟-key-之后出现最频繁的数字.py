#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-30 21:48:51
LastEditTime: 2022-03-30 21:54:49
Description: 
FilePath: 2190.数组中紧跟-key-之后出现最频繁的数字.py
"""
#
# @lc app=leetcode.cn id=2190 lang=python3
#
# [2190] 数组中紧跟 key 之后出现最频繁的数字
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        targetcount = defaultdict(int)
        for i in range(len(nums) - 1):
            if nums[i] == key:
                targetcount[nums[i + 1]] += 1
        print(targetcount)
        return max(targetcount.items(), key=lambda el: el[1])[0]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.mostFrequent(nums=[1, 100, 200, 1, 100], key=1)
    print(ans)
    ans = solution.mostFrequent(nums=[2, 2, 2, 2, 3], key=2)
    print(ans)
