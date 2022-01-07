#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-04 15:52:31
Description: 三除数
FilePath: 1952.三除数.py
'''
#
# @lc app=leetcode.cn id=1952 lang=python3
#
# [1952] 三除数
#

# @lc code=start

class Solution:
    def isPrime(self, num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def isThree(self, n: int) -> bool:
        for i in range(2, int(n ** 0.5) + 1):
            if self.isPrime(i) and i * i == n:
                return True
        return False
# @lc code=end

if __name__ == '__main__':   
    s = Solution()
    print(s.isThree(81))
