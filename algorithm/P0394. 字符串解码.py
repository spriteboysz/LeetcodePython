#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-19 23:41:38
LastEditTime: 2022-03-06 10:52:02
Description: 
FilePath: 394.字符串解码.py
"""


#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        decode, count = "", 0
        for item in s:
            if item.isdigit():
                count = count * 10 + int(item)
            if item.islower():
                decode += item
            if item == "[":
                stack.append((decode, count))
                decode, count = "", 0
            if item == "]":
                pre, count = stack.pop()
                decode, count = pre + decode * count, 0
        return decode


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.decodeString("3[a]2[bc]")
    print(ans)
    ans = solution.decodeString("3[a2[c]]")
    print(ans)
    ans = solution.decodeString("2[abc]3[cd]ef")
    print(ans)
    ans = solution.decodeString("abc3[cd]xyz")
    print(ans)
