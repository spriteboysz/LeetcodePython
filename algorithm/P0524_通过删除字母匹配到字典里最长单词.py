#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-14 21:53:02
LastEditTime: 2022-03-14 21:55:33
Description: 
FilePath: 524.通过删除字母匹配到字典里最长单词.py
"""
#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#

# @lc code=start
from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda el: (-len(el), el))

        for word in dictionary:
            i = 0
            for letter in s:
                if letter == word[i]:
                    i += 1
                if i == len(word):
                    return word
        return ""


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findLongestWord(
        s="abpcplea", dictionary=["ale", "apple", "monkey", "plea"]
    )
    print(ans)
    ans = solution.findLongestWord(s="abpcplea", dictionary=["a", "b", "c"])
    print(ans)
