#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-08 22:05
LastEditTime: 2022-06-08 22:05
Description:
FilePath: 面试题 08.09. 括号.py
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(left, right, bracket):
            if left > right:
                return
            if left == 0 and right == 0:
                brackets.append(bracket)
            if left > 0:
                dfs(left - 1, right, bracket + "(")
            if right > 0:
                dfs(left, right - 1, bracket + ")")

        brackets = []
        dfs(n, n, "")
        return brackets

if __name__ == '__main__':
    solution = Solution()
    ans = solution.generateParenthesis(3)
    print(ans)
