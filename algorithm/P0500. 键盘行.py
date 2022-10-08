#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-10 23:05:51
LastEditTime: 2022-01-10 23:18:59
Description: 
FilePath: 500.键盘行.py
'''
#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        words2 = []
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for word in words:
            for key in keyboard:
                for letter in set(list(word)):
                    if letter.lower() not in key:
                        break
                else:
                    words2.append(word)
                    break
        return words2
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.findWords(["Hello", "Dad"]))
