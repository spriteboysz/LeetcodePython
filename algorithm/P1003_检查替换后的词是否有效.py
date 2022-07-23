#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-13 23:26
LastEditTime: 2022-06-13 23:26
Description:
FilePath: 1003.检查替换后的词是否有效.py
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if len(stack) >= 2 and stack[-2] == "a" and stack[-1] == "b" and c == "c":
                stack.pop()
                stack.pop()
            else:
                stack.append(c)
        return not stack


if __name__ == '__main__':
    solution = Solution()
    ans = solution.isValid(s="aabcbc")
    print(ans)
    ans = solution.isValid(s="abcabcababcc")
    print(ans)
    ans = solution.isValid(s="abccba")
    print(ans)
