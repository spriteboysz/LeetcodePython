#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-15 19:13:30
LastEditTime: 2022-03-15 19:19:40
Description: 
FilePath: 792.匹配子序列的单词数.py
"""
#
# @lc app=leetcode.cn id=792 lang=python3
#
# [792] 匹配子序列的单词数
#

from collections import defaultdict
# @lc code=start
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        wordcount = defaultdict(int)
        for word in words:
            wordcount[word] += 1

        count = 0
        for word, num in wordcount.items():
            i = 0
            for item in s:
                if item == word[i]:
                    i += 1
                if i == len(word):
                    count += num
                    break
        return count


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.numMatchingSubseq(s="abcde", words=["a", "bb", "acd", "ace"])
    print(ans)
    ans = solution.numMatchingSubseq(
        s="dsahjpjauf", words=["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
    )
    print(ans)
