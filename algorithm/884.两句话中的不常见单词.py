#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-18 23:47:24
LastEditTime: 2022-01-18 23:53:55
Description: 
FilePath: 884.两句话中的不常见单词.py
'''
#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#

# @lc code=start
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1, words2 = s1.split(), s2.split()
        word1, word2 = set(words1), set(words2)
        uncommon = []
        for item in word1:
            if words1.count(item) == 1 and words2.count(item) == 0:
                uncommon.append(item)
        for item in word2:
            if words2.count(item) == 1 and words1.count(item) == 0:
                uncommon.append(item)
        return uncommon

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.uncommonFromSentences("apple apple", "banana"))
