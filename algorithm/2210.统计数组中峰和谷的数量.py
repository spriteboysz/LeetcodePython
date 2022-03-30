#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-30 22:28:24
LastEditTime: 2022-03-30 22:30:17
Description: 
FilePath: 2210.统计数组中峰和谷的数量.py
"""
#
# @lc app=leetcode.cn id=2210 lang=python3
#
# [2210] 统计数组中峰和谷的数量
#

# @lc code=start
from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        stack, count = [], 0
        for num in nums:
            if not stack or stack[-1] != num:
                stack.append(num)

        for i in range(1, len(stack) - 1):
            if stack[i - 1] < stack[i] > stack[i + 1]:
                count += 1
            elif stack[i - 1] > stack[i] < stack[i + 1]:
                count += 1
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.countHillValley([2, 4, 1, 1, 6, 5])
    print(ans)
    ans = solution.countHillValley([6, 6, 5, 5, 4, 1])
    print(ans)
