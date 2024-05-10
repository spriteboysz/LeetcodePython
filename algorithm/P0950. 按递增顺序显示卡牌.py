#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-09 23:32
FileName: algorithm
Description:P0950. 按递增顺序显示卡牌.py 
"""
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        ans = [deck[0]]
        for i in range(1, len(deck)):
            k = deck[i]
            ans = [ans[-1]] + ans[:-1]
            ans.insert(0, k)
        return ans


if __name__ == '__main__':
    print(Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
