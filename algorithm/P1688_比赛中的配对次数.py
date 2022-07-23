#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-23 22:27:50
LastEditTime: 2022-01-23 22:35:10
Description: 
FilePath: 1688.比赛中的配对次数.py
'''
#
# @lc app=leetcode.cn id=1688 lang=python3
#
# [1688] 比赛中的配对次数
#

# @lc code=start


class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
                count += n
            else:
                n = n // 2 + 1
                count += n - 1
        return count
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.numberOfMatches(7))