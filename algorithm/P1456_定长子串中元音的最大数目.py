#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-05 15:34:31
LastEditTime: 2022-03-05 15:43:21
Description: 
FilePath: 1456.定长子串中元音的最大数目.py
"""
#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#

# @lc code=start


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        maximum = count

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count += -1
            if s[i] in vowels:
                count += 1
                maximum = max(maximum, count)
            if maximum == k:
                break
        return maximum


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.maxVowels("abciiidef", 3)
    print(ans)
