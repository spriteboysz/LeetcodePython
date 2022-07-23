#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-02 23:10:34
LastEditTime: 2022-04-02 23:15:33
Description: 
FilePath: 22.括号生成.py
"""
#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(cur, left, right):
            if left == 0 and right == 0:
                parenthesis.append(cur)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur + "(", left - 1, right)
            if right > 0:
                dfs(cur + ")", left, right - 1)

        parenthesis, cur = [], ""
        dfs(cur, left=n, right=n)
        return parenthesis


# @lc code=end
