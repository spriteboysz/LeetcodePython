#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-14 19:57:24
LastEditTime: 2022-03-14 20:13:02
Description: 
FilePath: 784.字母大小写全排列.py
"""
#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        count = sum([item.isalpha() for item in s])
        permutation = []
        for i in range(2 ** count):
            perm, cur, j = "0" * (count - len(bin(i)[2:])) + bin(i)[2:], "", 0
            for item in s:
                if item.isalpha():
                    cur += item.lower() if perm[j] == "1" else item.upper()
                    j += 1
                else:
                    cur += item
            permutation.append(cur)
        return permutation


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.letterCasePermutation("a1b2")
    print(ans)
    ans = solution.letterCasePermutation("abcd")
    print(ans)
