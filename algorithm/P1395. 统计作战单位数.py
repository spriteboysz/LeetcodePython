#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-25 22:59:39
LastEditTime: 2022-02-25 23:04:25
Description: 
FilePath: 1395.统计作战单位数.py
"""
#
# @lc app=leetcode.cn id=1395 lang=python3
#
# [1395] 统计作战单位数
#

# @lc code=start
from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n, count = len(rating), 0
        for i in range(1, n):
            left, right = 0, 0
            for j in range(0, i):
                if rating[j] < rating[i]:
                    left += 1
            for k in range(i + 1, n):
                if rating[i] < rating[k]:
                    right += 1
            count += left * right + (i - left) * (n - i - 1 - right)
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.numTeams([2,5,3,4,1])
    print(ans)
