#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-04 16:38
LastEditTime: 2022-06-04 16:38
Description: 
FilePath: 1980.找出不同的二进制字符串.py
"""

from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        for i in range(2 ** n):
            cur = bin(i)[2:].rjust(n, "0")
            if cur not in nums:
                return cur
        return -1

    
if __name__ == '__main__':
    solution = Solution()
    ans = solution.findDifferentBinaryString(nums = ["111","011","001"])
    print(ans)
    