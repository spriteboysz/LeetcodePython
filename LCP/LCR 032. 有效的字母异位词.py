#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 15:56
FileName: LCP
Description:LCR 032. 有效的字母异位词.py 
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or s == t:
            return False
        alphabet = [0] * 26
        for i in range(len(s)):
            alphabet[ord(s[i]) - ord('a')] += 1
            alphabet[ord(t[i]) - ord('a')] -= 1
        return not any(alphabet)


if __name__ == '__main__':
    print(Solution().isAnagram(s="anagram", t="nagaram"))
    print(Solution().isAnagram(s="abc", t="abd"))
