#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-28 22:27:08
LastEditTime: 2022-01-28 22:33:45
Description: 
FilePath: 830.较大分组的位置.py
'''
#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#

# @lc code=start
from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        count = [1] * len(s)
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                count[i] = count[i - 1] + 1
                count[i - 1] = 0
        position = []
        for i, num in enumerate(count):
            if num >= 3:
                position.append([i - num + 1, i])
        return position
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.largeGroupPositions("abc"))
    print(s.largeGroupPositions("abcdddeeeeaabbbcd"))
    print(s.largeGroupPositions("aba"))