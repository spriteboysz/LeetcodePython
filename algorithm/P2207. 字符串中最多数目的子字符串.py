#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-13 22:25:57
LastEditTime: 2022-04-13 22:31:06
Description: 
FilePath: 2207.字符串中最多数目的子字符串.py
"""
#
# @lc app=leetcode.cn id=2207 lang=python3
#
# [2207] 字符串中最多数目的子字符串
#

# @lc code=start
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        def subseqCount(s):
            count, cur = 0, 0
            for item in s:
                if item == pattern[1]:
                    count += cur
                if item == pattern[0]:
                    cur += 1
            return count

        return max(subseqCount(pattern[0] + text), subseqCount(text + pattern[1]))


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.maximumSubsequenceCount("aabb", "ab")
    print(ans)
