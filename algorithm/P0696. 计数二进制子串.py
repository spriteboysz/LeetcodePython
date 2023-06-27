#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-01 23:14:26
LastEditTime: 2022-04-25 23:41:25
Description: 
FilePath: 696.计数二进制子串.py
"""


#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        group, count = [], 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                count += 1
            else:
                group.append(count)
                count = 1
        group.append(count)

        sum = 0
        for i in range(1, len(group)):
            sum += min(group[i - 1], group[i])
        return sum


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.countBinarySubstrings("00110011")
    print(ans)
