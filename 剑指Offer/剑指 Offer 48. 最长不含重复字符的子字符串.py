#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-19 21:26
LastEditTime: 2022-06-19 21:26
Description:
FilePath: 剑指 Offer 48. 最长不含重复字符的子字符串.py
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = len(set(s))
        while k > 0:
            for i in range(len(s) - k + 1):
                if len(set(s[i:i + k])) == len(s[i:i + k]):
                    return k
            k -= 1
        return 0


if __name__ == '__main__':
    solution = Solution()
    ans = solution.lengthOfLongestSubstring("pwwkew")
    print(ans)
