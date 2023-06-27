#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-22 22:21:06
LastEditTime: 2022-01-22 22:24:19
Description:
FilePath: 2000.反转单词前缀.py
"""


#
# @lc app=leetcode.cn id=2000 lang=python3
#
# [2000] 反转单词前缀
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            index = word.find(ch) + 1
            return word[:index][::-1] + word[index:]
        else:
            return word


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.reversePrefix("xyxzxe", "z"))
    print(s.reversePrefix("abcd", "z"))
