#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-19 23:08:36
LastEditTime: 2022-01-30 23:51:33
Description:
FilePath: 953.验证外星语词典.py
"""
#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

# @lc code=start
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        sequence = list(sorted(words, key=lambda el: tuple(
            order.index(letter) for letter in el)))
        return words == sequence
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.isAlienSorted(["word", "world", "row"],
          "worldabcefghijkmnpqstuvxyz"))
    print(s.isAlienSorted(words=["hello", "leetcode"],
          order="hlabcdefgijkmnopqrstuvwxyz"))
