#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-23 22:52:57
LastEditTime: 2022-01-23 23:01:49
Description: 
FilePath: 1668.最大重复子字符串.py
'''
#
# @lc app=leetcode.cn id=1668 lang=python3
#
# [1668] 最大重复子字符串
#

# @lc code=start
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        nums = ""
        print(sequence.replace(word, "1"))
        for item in sequence.replace(word, "1"):
            if item == "1":
                nums += item
            else:
                nums += " "
        print(nums)
        if "1" in nums:
            return max(map(len, nums.strip().split()))
        else:
            return 0
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba"))