#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-16 22:42:04
LastEditTime: 2022-02-16 23:10:23
Description: 
FilePath: 77.组合.py
"""
#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = [[]]
        for i in range(1, n + 1):
            for j in range(len(comb)):
                comb.append(comb[j] + [i])
        return list(filter(lambda el: len(el) == k, comb))


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.combine(4, 2)
    print(ans)
