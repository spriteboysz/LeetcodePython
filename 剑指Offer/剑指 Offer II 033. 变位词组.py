#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-16 23:28:22
LastEditTime: 2022-05-16 23:28:25
Description: 
FilePath: 剑指 Offer II 033. 变位词组.py
"""

from typing import List
from collections import defaultdict
from string import ascii_lowercase as lowercase


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for str in strs:
            cur = [0] * 26
            for item in str:
                cur[lowercase.index(item)] += 1
            dic[tuple(cur)].append(str)
        return list(dic.values())


if __name__ == "__main__":
    solution = Solution()
    ans = solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])
    print(ans)
