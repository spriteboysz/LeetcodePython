#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-28 21:47:11
LastEditTime: 2022-01-28 21:58:29
Description:
FilePath: 1160.拼写单词.py
"""
#
# @lc app=leetcode.cn id=1160 lang=python3
#
# [1160] 拼写单词
#

# @lc code=start
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic = {letter: chars.count(letter) for letter in set(chars)}
        count = 0
        for word in words:
            for letter in set(word):
                if letter not in dic.keys() or word.count(letter) > dic[letter]:
                    break
            else:
                count += len(word)
        return count
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.countCharacters(["cat", "bt", "hat", "tree"], "atach"))
    print(s.countCharacters(["hello", "world", "leetcode"], "welldonehoneyr"))
