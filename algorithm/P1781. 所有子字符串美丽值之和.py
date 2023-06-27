#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-12 15:55
LastEditTime: 2022-06-12 15:55
Description:
FilePath: 1781.所有子字符串美丽值之和.py
"""

from collections import defaultdict


class Solution:
    def beautySum(self, s: str) -> int:
        beauty = 0
        for i in range(len(s)):
            dic = defaultdict(int)
            for j in range(i, len(s)):
                dic[s[j]] += 1
                beauty += max(dic.values()) - min(dic.values())
        return beauty


if __name__ == '__main__':
    solution = Solution()
    ans = solution.beautySum("aabcb")
    print(ans)
    ans = solution.beautySum(s="aabcbaa")
    print(ans)
