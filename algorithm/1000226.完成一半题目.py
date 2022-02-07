#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-07 23:46:49
LastEditTime: 2022-02-07 23:56:54
Description: 
FilePath: 1000226.完成一半题目.py
'''
#
# @lc app=leetcode.cn id=1000226 lang=python3
#
# [LCS 02] 完成一半题目
#

# @lc code=start
from typing import List


class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        types = [0] * 1001
        for question in questions:
            types[question] += 1
        types.sort(reverse=True)
        count = 0
        print(types[:len(questions)])
        for i, type in enumerate(types):
            count += type
            if count >= len(questions) / 2:
                return i + 1
        return -1
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.halfQuestions([13, 8, 3, 7, 5, 6, 11, 12, 3, 6, 6, 11]))
    print(s.halfQuestions([1, 5, 1, 3, 4, 5, 2, 5, 3, 3, 8, 6]))
    print(s.halfQuestions([2, 1, 6, 2]))
