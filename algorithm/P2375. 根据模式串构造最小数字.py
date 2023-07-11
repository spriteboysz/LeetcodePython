#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-10 23:14
FileName: algorithm/P2375. 根据模式串构造最小数字.py
Description: 
"""


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        nums = [0]
        for i, c in enumerate(pattern):
            if c == 'I':
                nums.append(nums[-1] + 2 ** 8)
            else:
                nums.append(nums[-1] - 2 ** (8 - i - 1))
        return ''.join(str(i + 1) for i in sorted(range(len(nums)), key=lambda i: nums[i]))


if __name__ == '__main__':
    print(Solution().smallestNumber(pattern="IIIDIDDD"))
