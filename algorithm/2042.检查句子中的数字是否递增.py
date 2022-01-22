#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-22 21:25:57
LastEditTime: 2022-01-22 21:31:15
Description: 
FilePath: 2042.检查句子中的数字是否递增.py
'''
#
# @lc app=leetcode.cn id=2042 lang=python3
#
# [2042] 检查句子中的数字是否递增
#

# @lc code=start


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = list(map(int, filter(lambda el: el.isdigit(), s.split())))
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                return False
        return True
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.areNumbersAscending("hello world 5 x 5"))
