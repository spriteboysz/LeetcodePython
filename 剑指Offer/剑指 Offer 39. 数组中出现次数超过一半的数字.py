#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-04 22:19:10
LastEditTime: 2022-02-04 22:35:12
Description:
FilePath: 100310.数组中出现次数超过一半的数字.py
"""
#
# @lc app=leetcode.cn id=100310 lang=python3
#
# [剑指 Offer 39] 数组中出现次数超过一半的数字
#

# @lc code=start
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = dict()
        for num in nums:
            if num in count.keys():
                count[num] += 1
            else:
                count[num] = 1
        key, value = sorted(count.items(), key=lambda kv: (
            kv[1], kv[0]), reverse=True)[0]
        if value > len(nums) // 2:
            return key
        else:
            return -1
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))
