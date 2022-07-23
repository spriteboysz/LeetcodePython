#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-28 22:04:58
LastEditTime: 2022-02-18 22:05:09
Description: 
FilePath: 1047.删除字符串中的所有相邻重复项.py
"""
#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for letter in s:
            if stack == []:
                stack.append(letter)
            elif stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates("aababaab"))
