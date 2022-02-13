#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-13 16:57:15
LastEditTime: 2022-02-13 17:30:47
Description: 
FilePath: 202.快乐数.py
'''
#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start


class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n != 1:
            if n not in nums:
                nums.add(n)
            else:
                return False
            n = sum(map(lambda el: int(el) ** 2, str(n)))   
        return True

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    arguments = [19, 2]
    for i, args in enumerate(arguments):
        print("=== {:02d} INPUT ===".format(i + 1))
        print(args)
        print("=== DEBUG ===")
        answer = solution.isHappy(args)
        print("=== OUTPUT ===")
        print(answer)
