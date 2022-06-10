#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-10 22:31
LastEditTime: 2022-06-10 22:31
Description:
FilePath: 剑指 Offer II 085. 生成匹配的括号.py
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrace(left, right):
            if left < 0 or right < 0 or left > right:
                return
            if left == 0 and right == 0:
                brackets.append("".join(path))
                return
            path.append("(")
            backtrace(left - 1, right)
            path.pop()
            path.append(")")
            backtrace(left, right - 1)
            path.pop()

        brackets, path = [], []
        backtrace(n, n)
        return brackets


if __name__ == '__main__':
    solution = Solution()
    ans = solution.generateParenthesis(3)
    print(ans)
