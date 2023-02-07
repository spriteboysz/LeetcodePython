#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-16 22:16:43
LastEditTime: 2022-04-16 22:26:17
Description: 
FilePath: 3.无重复字符的最长子串.py
"""
#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 1 if s else 0
        i, j = 0, 0
        while j < len(s) - 1:
            j += 1
            index = s[i:j].find(s[j])
            if index != -1:
                i += index + 1
            else:
                maximum = max(j - i + 1, maximum)
        return maximum


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.lengthOfLongestSubstring("pwwkew")
    print(ans)
