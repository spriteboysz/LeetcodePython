#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-06 15:48:54
LastEditTime: 2022-02-06 16:14:21
Description:
FilePath: 409.最长回文串.py
"""


#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = []
        for item in set(s):
            count.append(s.count(item))
        odd = list(filter(lambda el: el % 2 != 0, count))
        return sum(count) - len(odd) + int(len(odd) != 0)


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))
    print(s.longestPalindrome("a"))
    print(s.longestPalindrome("bb"))