#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-03 23:33:48
LastEditTime: 2022-03-03 23:35:45
Description: 
FilePath: 1017.负二进制转换.py
"""
#
# @lc app=leetcode.cn id=1017 lang=python3
#
# [1017] 负二进制转换
#

# @lc code=start
class Solution:
    def baseNeg2(self, n: int) -> str:
        neg2 = ""
        while n:
            # n, mod = divmod(n, -2)
            n, mod = -(n // 2), n % 2
            neg2 += str(mod)
        return neg2[::-1] if neg2 else "0"


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.baseNeg2(2)
    print(ans)
    ans = solution.baseNeg2(3)
    print(ans)
