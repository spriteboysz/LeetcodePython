#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-13 22:37:07
LastEditTime: 2022-04-13 22:41:27
Description: 
FilePath: 2216.美化数组的最少删除数.py
"""
#
# @lc app=leetcode.cn id=2216 lang=python3
#
# [2216] 美化数组的最少删除数
#

# @lc code=start
from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if len(stack) % 2 == 0 or stack[-1] != num:
                stack.append(num)

        return len(nums) - (len(stack) - len(stack) % 2)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minDeletion([1, 1, 2, 3, 5])
    print(ans)
    ans = solution.minDeletion([1, 1, 2, 2, 3, 3])
    print(ans)
