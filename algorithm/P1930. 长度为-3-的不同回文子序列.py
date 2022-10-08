#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-11 23:41:45
LastEditTime: 2022-02-11 23:47:57
Description: 
FilePath: 1930.长度为-3-的不同回文子序列.py
'''
#
# @lc app=leetcode.cn id=1930 lang=python3
#
# [1930] 长度为 3 的不同回文子序列
#

# @lc code=start


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        counts = dict()
        for i, item in enumerate(s):
            if item in counts:
                counts[item][1] = i
            else:
                counts[item] = [i, 0]
        count = 0
        for item in filter(lambda el: el[1], counts.values()):
            count += len(set(s[item[0]+1:item[1]]))
        return count

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.countPalindromicSubsequence("adc"))
    print(s.countPalindromicSubsequence("bbcbaba"))
