#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-15 22:13:48
LastEditTime: 2022-04-15 22:17:01
Description: 
FilePath: 1638.统计只差一个字符的子串数目.py
"""


#
# @lc app=leetcode.cn id=1638 lang=python3
#
# [1638] 统计只差一个字符的子串数目
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        count = 0
        for i in range(m):
            for j in range(n):
                diff, k = 0, 0
                while i + k < m and j + k < n:
                    if s[i + k] != t[j + k]:
                        diff += 1
                    if diff > 2:
                        break
                    if diff == 1:
                        count += 1
                    k += 1
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.countSubstrings("abe", "bbc")
    print(ans)
