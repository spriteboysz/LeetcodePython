#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-29 23:10:04
LastEditTime: 2022-04-29 23:13:39
Description: 
FilePath: 1558.得到目标数组的最少函数调用次数.py
"""
#
# @lc app=leetcode.cn id=1558 lang=python3
#
# [1558] 得到目标数组的最少函数调用次数
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while True:
            for i, num in enumerate(nums):
                if num & 1:
                    count += 1
                nums[i] >>= 1
            if sum(nums) == 0:
                break
            count += 1
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minOperations([4, 2, 5])
    print(ans)
