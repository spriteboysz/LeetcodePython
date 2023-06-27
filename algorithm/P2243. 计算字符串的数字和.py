#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-20 22:11:27
LastEditTime: 2022-04-20 22:14:55
Description: 
FilePath: 2243.计算字符串的数字和.py
"""


#
# @lc app=leetcode.cn id=2243 lang=python3
#
# [2243] 计算字符串的数字和
#

# @lc code=start
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            cur = ""
            for i in range(0, len(s), k):
                cur += str(sum(map(int, list(s[i: i + k]))))
            s = cur
        return s


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.digitSum(s="11111222223", k=3)
    print(ans)
    ans = solution.digitSum(s="00000000", k=3)
    print(ans)
