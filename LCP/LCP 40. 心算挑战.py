#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-09 23:41
LastEditTime: 2022-06-09 23:41
Description:
FilePath: LCP 40. 心算挑战.py
"""

from typing import List


class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        if cnt > len(cards):
            return 0

        odd, even, score = [0], [0], 0
        cards.sort(reverse=True)
        for card in cards:
            if card % 2:
                odd.append(card + odd[-1])
            else:
                even.append(card + even[-1])

        for i in range(0, min(len(odd) - 1, cnt) + 1, 2):
            if len(even) - 1 >= cnt - i:
                score = max(score, odd[i] + even[cnt - i])

        return score


if __name__ == '__main__':
    solution = Solution()
    ans = solution.maxmiumScore(cards=[1, 2, 8, 9], cnt=3)
    print(ans)
