#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-27 22:23:26
LastEditTime: 2022-02-27 22:31:58
Description: 
FilePath: 2007.从双倍数组中还原原数组.py
"""
#
# @lc app=leetcode.cn id=2007 lang=python3
#
# [2007] 从双倍数组中还原原数组
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        nums = defaultdict(int)
        for item in changed:
            nums[item] += 1
        original = []
        for item in sorted(changed):
            if nums[item] > 0:
                if nums[item] > nums[2 * item]:
                    return []
                original.append(item)
                nums[item] -= 1
                nums[2 * item] -= 1
        return original


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.findOriginalArray([1, 3, 4, 2, 6, 8])
    print(ans)
