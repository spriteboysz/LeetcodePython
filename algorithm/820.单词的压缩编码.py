#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-15 19:32:47
LastEditTime: 2022-03-15 19:33:33
Description: 
FilePath: 820.单词的压缩编码.py
"""
#
# @lc app=leetcode.cn id=820 lang=python3
#
# [820] 单词的压缩编码
#

# @lc code=start
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        wordset = set(words)
        for word in words:
            for j in range(1, len(word)):
                wordset.discard(word[j:])

        count = 0
        for word in wordset:
            count += len(word) + 1
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minimumLengthEncoding(words=["time", "me", "bell"])
    print(ans)
