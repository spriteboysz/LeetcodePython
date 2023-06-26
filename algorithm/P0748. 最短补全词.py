#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-28 22:50:33
LastEditTime: 2022-01-28 22:59:15
Description:
FilePath: 748.最短补全词.py
"""
#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短补全词
#

# @lc code=start
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words = sorted(words, key=lambda el: len(el))
        dic = {k: licensePlate.lower().count(k)
               for k in set(licensePlate.lower()) if k.isalpha()}
        for word in words:
            for letter in dic.keys():
                if letter not in word or dic[letter] > word.count(letter):
                    break
            else:
                return word
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.shortestCompletingWord("1s3 PSt", [
          "step", "steps", "stripe", "stepple"]))
