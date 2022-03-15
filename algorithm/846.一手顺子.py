#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-15 20:03:33
LastEditTime: 2022-03-15 20:09:32
Description: 
FilePath: 846.一手顺子.py
"""
#
# @lc app=leetcode.cn id=846 lang=python3
#
# [846] 一手顺子
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        cardcount = defaultdict(int)
        for card in hand:
            cardcount[card] += 1

        for card in sorted(hand):
            if cardcount[card] >= 1:
                for i in range(card, card + groupSize):
                    cardcount[i] -= 1
                    if cardcount[i] < 0:
                        return False
        return True


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3)
    print(ans)
