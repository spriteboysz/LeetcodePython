#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-09 22:16:24
LastEditTime: 2022-02-09 22:26:03
Description:
FilePath: 1807.替换字符串中的括号内容.py
"""
#
# @lc app=leetcode.cn id=1807 lang=python3
#
# [1807] 替换字符串中的括号内容
#

# @lc code=start
from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge = dict(knowledge)
        ans = ""
        flag, variable = False, ""
        for item in s:
            if item == "(":
                flag = True
                continue
            elif item == ")":
                ans += knowledge[variable] if variable in knowledge else "?"
                flag, variable = False, ""
                continue
            if flag:
                variable += item
            else:
                ans += item
        return ans

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.evaluate("(name)is(age)yearsold",
          [["name", "bob"], ["age", "two"]]))
    print(s.evaluate("hi(name)", [["a", "b"]]))
    print(s.evaluate("(a)(a)(a)aaa", [["a", "yes"]]))
    print(s.evaluate(s="(a)(b)", knowledge=[["a", "b"], ["b", "a"]]))
