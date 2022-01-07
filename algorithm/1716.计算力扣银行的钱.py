#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-04 22:54:36
Description: 
FilePath: 1716.计算力扣银行的钱.py
'''
#
# @lc app=leetcode.cn id=1716 lang=python3
#
# [1716] 计算力扣银行的钱
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        count = 0
        for i in range(0, n):
            basic = i // 7 + 1
            count += basic + i % 7

        return count
                
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.totalMoney(20))

