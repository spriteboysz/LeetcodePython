#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-05 16:45:57
LastEditTime: 2022-03-05 16:56:27
Description: 
FilePath: 1333.餐厅过滤器.py
"""
#
# @lc app=leetcode.cn id=1333 lang=python3
#
# [1333] 餐厅过滤器
#

# @lc code=start
from typing import List


class Solution:
    def filterRestaurants(
        self,
        restaurants: List[List[int]],
        veganFriendly: int,
        maxPrice: int,
        maxDistance: int,
    ) -> List[int]:
        if veganFriendly:
            restaurants = filter(lambda el: el[2], restaurants)

        restaurants = filter(
            lambda el: el[3] <= maxPrice and el[4] <= maxDistance, restaurants
        )

        return [
            el[0]
            for el in sorted(restaurants, key=lambda el: (el[1], el[0]), reverse=True)
        ]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.filterRestaurants(
        restaurants=[
            [1, 4, 1, 40, 10],
            [2, 8, 0, 50, 5],
            [3, 8, 1, 30, 4],
            [4, 10, 0, 10, 3],
            [5, 1, 1, 15, 1],
        ],
        veganFriendly=1,
        maxPrice=50,
        maxDistance=10,
    )
    print(ans)

    ans = solution.filterRestaurants(
        restaurants=[
            [1, 4, 1, 40, 10],
            [2, 8, 0, 50, 5],
            [3, 8, 1, 30, 4],
            [4, 10, 0, 10, 3],
            [5, 1, 1, 15, 1],
        ],
        veganFriendly=0,
        maxPrice=50,
        maxDistance=10,
    )
    print(ans)
    ans = solution.filterRestaurants(
        restaurants=[
            [1, 4, 1, 40, 10],
            [2, 8, 0, 50, 5],
            [3, 8, 1, 30, 4],
            [4, 10, 0, 10, 3],
            [5, 1, 1, 15, 1],
        ],
        veganFriendly=0,
        maxPrice=30,
        maxDistance=3,
    )
    print(ans)
