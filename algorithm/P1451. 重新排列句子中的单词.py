#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-28 23:55:19
LastEditTime: 2022-02-28 23:59:37
Description: 
FilePath: 1451.重新排列句子中的单词.py
"""


#
# @lc app=leetcode.cn id=1451 lang=python3
#
# [1451] 重新排列句子中的单词
#

# @lc code=start
class Solution:
    def arrangeWords(self, text: str) -> str:
        text = sorted(text.lower().split(), key=len)
        return (" ".join(text)).capitalize()


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.arrangeWords("Leetcode is cool")
    print(ans)
    ans = solution.arrangeWords("Keep calm and code on")
    print(ans)
    ans = solution.arrangeWords("To be or not to be")
    print(ans)
