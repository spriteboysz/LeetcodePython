#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-18 23:37:45
LastEditTime: 2022-04-18 23:50:39
Description: 
FilePath: 1750.删除字符串两端相同字符后的最短长度.py
"""


#
# @lc app=leetcode.cn id=1750 lang=python3
#
# [1750] 删除字符串两端相同字符后的最短长度
#

# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                break
            c = s[left]
            while left <= right and s[left] == c:
                left += 1
            while left <= right and s[right] == c:
                right -= 1

        return right - left + 1


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minimumLength("ca")
    print(ans)
    ans = solution.minimumLength("cabaabac")
    print(ans)
    ans = solution.minimumLength("aabccabba")
    print(ans)
