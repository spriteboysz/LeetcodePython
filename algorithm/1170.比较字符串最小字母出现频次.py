#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-05 23:29:16
LastEditTime: 2022-03-05 23:36:32
Description: 
FilePath: 1170.比较字符串最小字母出现频次.py
"""
#
# @lc app=leetcode.cn id=1170 lang=python3
#
# [1170] 比较字符串最小字母出现频次
#

# @lc code=start
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        frequency_queries, frequency_words = [], []
        for query in queries:
            frequency_queries.append(query.count(min(query)))
        for word in words:
            frequency_words.append(word.count(min(word)))
        # print(frequency_queries, frequency_words)
        count = [0] * len(queries)
        for i, fq in enumerate(frequency_queries):
            for fw in frequency_words:
                if fw > fq:
                    count[i] += 1
        return count


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.numSmallerByFrequency(["cbd"], ["zaaaz"])
    print(ans)
    ans = solution.numSmallerByFrequency(
        queries=["bbb", "cc"], words=["a", "aa", "aaa", "aaaa"]
    )
    print(ans)
