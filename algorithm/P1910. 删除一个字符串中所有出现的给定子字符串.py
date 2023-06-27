#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-14 00:01:43
LastEditTime: 2022-03-14 00:07:57
Description: 
FilePath: 1910.删除一个字符串中所有出现的给定子字符串.py
"""


#
# @lc app=leetcode.cn id=1910 lang=python3
#
# [1910] 删除一个字符串中所有出现的给定子字符串
#

# @lc code=start
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack, n = [], len(part)
        for item in s:
            stack.append(item)
            if "".join(stack[-n:]) == part:
                stack = stack[:-n]
        return "".join(stack)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.removeOccurrences(s="daabcbaabcbc", part="abc")
    print(ans)
    ans = solution.removeOccurrences(s="axxxxyyyyb", part="xy")
    print(ans)
