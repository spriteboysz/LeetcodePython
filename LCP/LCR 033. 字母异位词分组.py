#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 16:04
FileName: LCP
Description:LCR 033. 字母异位词分组.py 
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {s: "".join(sorted(s)) for s in strs}
        group = defaultdict(list)
        for s in strs:
            group[dic[s]].append(s)
        return list(group.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
