#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-28 22:58:22
LastEditTime: 2022-02-28 23:07:59
Description: 
FilePath: 1525.字符串的好分割数目.py
'''
#
# @lc app=leetcode.cn id=1525 lang=python3
#
# [1525] 字符串的好分割数目
#

# @lc code=start
from string import ascii_lowercase

class Solution:
    def numSplits(self, s: str) -> int:
        left, right = [0] * 26, [0] * 26
        for letter in s:
            right[ascii_lowercase.index(letter)] += 1

        count = 0
        for letter in s:
            left[ascii_lowercase.index(letter)] += 1
            right[ascii_lowercase.index(letter)] -= 1
            if left.count(0) == right.count(0):
                count += 1
        return count

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.numSplits("aacaba")
    print(ans)
    ans = solution.numSplits("abcd")
    print(ans)
    ans = solution.numSplits("a")
    print(ans)
    ans = solution.numSplits("acbadbaada")
    print(ans)

