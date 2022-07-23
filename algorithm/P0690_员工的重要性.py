#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-26 23:44:09
LastEditTime: 2022-04-27 00:02:38
Description: 
FilePath: 690.员工的重要性.py
"""
#
# @lc app=leetcode.cn id=690 lang=python3
#
# [690] 员工的重要性
#

# @lc code=start
from typing import List

# # Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        dic = {employee.id: employee for employee in employees}
        queue, importance = dic[id].subordinates, dic[id].importance
        while queue:
            cur = queue.pop(0)
            queue.extend(dic[cur].subordinates)
            importance += dic[cur].importance
        return importance


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1)
    print(ans)
