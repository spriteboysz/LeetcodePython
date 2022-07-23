#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-03-03 23:25:50
LastEditTime: 2022-03-03 23:27:02
Description: 
FilePath: 1016.子串能表示从-1-到-n-数字的二进制串.py
'''
#
# @lc app=leetcode.cn id=1016 lang=python3
#
# [1016] 子串能表示从 1 到 N 数字的二进制串
#

# @lc code=start
class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1, n + 1):
            if bin(i)[2:] not in s:
                return False
        return True
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.queryString("0110", 3)
    print(ans)

