#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-22 22:14:38
LastEditTime: 2022-01-22 22:16:52
Description: 
FilePath: 2011.执行操作后的变量值.py
'''
#
# @lc app=leetcode.cn id=2011 lang=python3
#
# [2011] 执行操作后的变量值
#

# @lc code=start
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for item in operations:
            if "+" in item:
                count += 1
            elif "-" in item:
                count -= 1
        return count

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.finalValueAfterOperations(["++X", "++X", "X++"]))
