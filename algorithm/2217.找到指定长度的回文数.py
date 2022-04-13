#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-13 21:56:38
LastEditTime: 2022-04-13 22:01:28
Description: 
FilePath: 2217.找到指定长度的回文数.py
"""
#
# @lc app=leetcode.cn id=2217 lang=python3
#
# [2217] 找到指定长度的回文数
#

# @lc code=start
from typing import List


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        base = 10 ** ((intLength - 1) // 2)
        palindrome = [-1] * len(queries)
        for i, query in enumerate(queries):
            if query <= 9 * base:
                cur = str(base + query - 1)  # 回文数左半部分
                cur += cur[-2::-1] if intLength % 2 else cur[::-1]
                palindrome[i] = int(cur)
        return palindrome


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.kthPalindrome([2, 4, 6], 4)
    print(ans)
