#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-22 00:00:12
LastEditTime: 2022-01-22 00:07:50
Description: 
FilePath: 2047.句子中的有效单词数.py
'''
#
# @lc app=leetcode.cn id=2047 lang=python3
#
# [2047] 句子中的有效单词数
#

# @lc code=start

class Solution:
    def countValidWords(self, sentence: str) -> int:
        count = 0
        for word in sentence.split():
            if sum(map(lambda el:word.count(el), "0123456789")) == 0:
                print(word)
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.countValidWords("!this  1-s b8d!"))

