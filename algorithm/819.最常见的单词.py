#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-28 23:13:48
Description: 
FilePath: 819.最常见的单词.py
'''
#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for item in ["!", "?", "'", ",", ";", "."]:
            paragraph = paragraph.replace(item, "")
        for item in banned:
            paragraph = paragraph.replace(item, "")
            
        lst = paragraph.lower().split()
        sorted(Counter(lst))
        

        
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    m = s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    print(m)
