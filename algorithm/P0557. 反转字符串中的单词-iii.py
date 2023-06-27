#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-07 22:26:11
LastEditTime: 2022-01-11 23:11:41
Description:
FilePath: 557.反转字符串中的单词-iii.py
"""


#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        lst = []
        for item in s.split():
            lst.append(item[::-1])
        return " ".join(lst)


# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))
