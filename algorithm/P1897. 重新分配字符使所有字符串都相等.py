#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-23 00:00:49
LastEditTime: 2022-01-23 00:07:22
Description: 
FilePath: 1897.重新分配字符使所有字符串都相等.py
'''
#
# @lc app=leetcode.cn id=1897 lang=python3
#
# [1897] 重新分配字符使所有字符串都相等
#

# @lc code=start
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        sentence = "".join(words)
        return all(map(lambda el: sentence.count(el) % len(words) == 0, set(sentence)))

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.makeEqual(["abc", "aabc", "bc"]))
    print(s.makeEqual(["ab", "a"]))
