#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-17 23:25:01
LastEditTime: 2022-02-17 23:27:23
Description: 
FilePath: 791.自定义字符串排序.py
"""
#
# @lc app=leetcode.cn id=791 lang=python3
#
# [791] 自定义字符串排序
#

# @lc code=start
from string import ascii_lowercase


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order += "".join((sorted(list(set(ascii_lowercase) - set(order)))))
        return "".join(sorted(s, key=lambda el: order.index(el)))


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.customSortString("cba", "abcd")
    print(ans)
