#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-18 23:21:02
LastEditTime: 2022-04-18 23:24:08
Description: 
FilePath: 1754.构造字典序最大的合并字符串.py
"""
#
# @lc app=leetcode.cn id=1754 lang=python3
#
# [1754] 构造字典序最大的合并字符串
#

# @lc code=start
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ""
        while word1 or word2:
            if word1 > word2:
                merge += word1[0]
                word1 = word1[1:]
            else:
                merge += word2[0]
                word2 = word2[1:]
        return merge


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.largestMerge(word1="cabaa", word2="bcaaa")
    print(ans)
    ans = solution.largestMerge("abcabc", "abdcaba")
    print(ans)
