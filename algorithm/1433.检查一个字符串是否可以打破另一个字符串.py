#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-03-01 00:03:58
LastEditTime: 2022-03-01 22:45:11
Description: 
FilePath: 1433.检查一个字符串是否可以打破另一个字符串.py
'''
#
# @lc app=leetcode.cn id=1433 lang=python3
#
# [1433] 检查一个字符串是否可以打破另一个字符串
#

# @lc code=start
from string import ascii_lowercase

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        interval1, interval2 = [], []
        for l1, l2 in zip(sorted(s1), sorted(s2)):
            interval1.append(l1 >= l2)
            interval2.append(l1 <= l2)
        return all(interval1) or all(interval2)

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.checkIfCanBreak("abc", "xya")
    print(ans)
    ans = solution.checkIfCanBreak("abe", "acd")
    print(ans)
    print(solution.checkIfCanBreak("leetcodee", "interview"))

