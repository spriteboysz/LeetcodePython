#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-04 22:39:39
LastEditTime: 2022-02-04 22:42:02
Description: 
FilePath: 100296.打印从-1-到最大的n位数.py
'''
#
# @lc app=leetcode.cn id=100296 lang=python3
#
# [剑指 Offer 17] 打印从1到最大的n位数
#

# @lc code=start
from typing import List
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return [i for i in range(1, 10 ** n)]
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.printNumbers(2))

