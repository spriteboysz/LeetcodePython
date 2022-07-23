#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-16 23:47:47
LastEditTime: 2022-01-16 23:55:03
Description: 
FilePath: 806.写字符串需要的行数.py
'''
#
# @lc app=leetcode.cn id=806 lang=python3
#
# [806] 写字符串需要的行数
#

from string import ascii_lowercase
# @lc code=start
from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line, cur = 1, 0
        for item in s:
            width = widths[ascii_lowercase.index(item)]
            if cur + width > 100:
                line += 1
                cur = width
            else:
                cur += width
        return [line, cur]
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfLines([4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
          10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], "bbbcccdddaaa"))
