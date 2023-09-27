#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-09-24 22:32
FileName: algorithm
Description:P2833. 距离原点最远的点.py 
"""


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        distance, other = 0, 0
        for move in moves:
            if move == 'L':
                distance -= 1
            elif move == 'R':
                distance += 1
            else:
                other += 1
        return abs(distance) + other


if __name__ == '__main__':
    print(Solution().furthestDistanceFromOrigin(moves="L_RL__R"))
