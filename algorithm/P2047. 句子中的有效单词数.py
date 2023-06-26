#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-16 00:07:56
LastEditTime: 2022-03-01 23:45:40
Description:
FilePath: 2047.句子中的有效单词数.py
"""

#
# @lc app=leetcode.cn id=2047 lang=python3
#
# [2047] 句子中的有效单词数
#

# @lc code=start
import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        count = 0
        for word in sentence.split():
            count += bool(re.match(r"[a-z]*([a-z]-[a-z]+)?[!.,]?$", word))
        return count


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.countValidWords("!this  1-s b8d!"))
    print(s.countValidWords("cat and   dog"))
