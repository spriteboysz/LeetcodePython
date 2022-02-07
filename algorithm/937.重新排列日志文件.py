#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-07 22:33:26
LastEditTime: 2022-02-07 22:44:42
Description: 
FilePath: 937.重新排列日志文件.py
'''
#
# @lc app=leetcode.cn id=937 lang=python3
#
# [937] 重新排列日志文件
#

# @lc code=start
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        chrlog = list(filter(lambda el: el.split()[-1].islower(), logs))
        numlog = list(filter(lambda el: el.split()[-1].isdigit(), logs))
        chrlog.sort(key=lambda el: (el.split()[1:], el.split()[0]))
        return chrlog + numlog

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.reorderLogFiles(logs=[
          "dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
    print(s.reorderLogFiles(
        logs=["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))
