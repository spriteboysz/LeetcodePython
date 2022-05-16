#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-16 23:05:17
LastEditTime: 2022-05-16 23:07:25
Description: 
FilePath: 剑指 Offer II 032. 有效的变位词.py
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return False if s == t else sorted(list(s)) == sorted(list(t))


if __name__ == "__main__":
    solution = Solution()
    ans = solution.isAnagram(s="anagram", t="nagaram")
    print(ans)
    ans = solution.isAnagram("a", "a")
    print(ans)
