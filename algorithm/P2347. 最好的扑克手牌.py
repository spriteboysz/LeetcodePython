#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-26 22:58
FileName: algorithm/P2347. 最好的扑克手牌.py
Description: 
"""
from collections import defaultdict
from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        hash = defaultdict(int)
        for rank in ranks:
            hash[rank] += 1
        maximum = max(hash.values())
        if maximum >= 3:
            return "Three of a Kind"
        elif maximum == 2:
            return "Pair"
        else:
            return "High Card"


if __name__ == '__main__':
    ranks = [4, 4, 2, 4, 4]
    suits = ["d", "a", "a", "b", "c"]
    print(Solution().bestHand(ranks, suits))
