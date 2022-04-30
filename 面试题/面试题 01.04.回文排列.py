#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-04 15:26:35
LastEditTime: 2022-02-04 15:32:41
Description: 
FilePath: 100184.回文排列.py
'''
#
# @lc app=leetcode.cn id=100184 lang=python3
#
# [面试题 01.04] 回文排列
#

# @lc code=start


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = []
        for item in set(s):
            count.append(s.count(item))
        return len(list(filter(lambda el: el % 2 == 1, count))) <= 1
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.canPermutePalindrome("tactcoa"))
    print(s.canPermutePalindrome("code"))
