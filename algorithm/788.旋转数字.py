#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-27 16:55:52
LastEditTime: 2022-02-27 22:25:26
Description: 
FilePath: 788.旋转数字.py
'''
#
# @lc app=leetcode.cn id=788 lang=python3
#
# [788] 旋转数字
#

# @lc code=start
class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            for num in list(str(i)):
                if int(num) not in [0, 1, 2, 5, 8, 6, 9]:
                    break
            else:
                print(num)
                count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.rotatedDigits(10)
    print(ans)

