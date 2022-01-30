#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-30 22:34:26
LastEditTime: 2022-01-30 22:40:37
Description: 
FilePath: 1700.无法吃午餐的学生数量.py
'''
#
# @lc app=leetcode.cn id=1700 lang=python3
#
# [1700] 无法吃午餐的学生数量
#

# @lc code=start
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for sandwich in sandwiches:
            if sandwich in students:
                students.remove(sandwich)
            else:
                return len(students)
        return 0
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
