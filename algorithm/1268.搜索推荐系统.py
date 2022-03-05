#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-06 00:03:40
LastEditTime: 2022-03-06 00:09:06
Description: 
FilePath: 1268.搜索推荐系统.py
"""
#
# @lc app=leetcode.cn id=1268 lang=python3
#
# [1268] 搜索推荐系统
#

# @lc code=start
from typing import List


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        products = sorted(products)
        suggested = []
        for i in range(len(searchWord)):
            cur = searchWord[: i + 1]
            products = list(filter(lambda el: el.startswith(cur), products))
            suggested.append(products[:3])
        return suggested


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.suggestedProducts(
        products=["mobile", "mouse", "moneypot", "monitor", "mousepad"],
        searchWord="mouse",
    )
    print(ans)
    ans = solution.suggestedProducts(products=["havana"], searchWord="havana")
    print(ans)
    ans = solution.suggestedProducts(
        products=["bags", "baggage", "banner", "box", "cloths"], searchWord="bags"
    )
    print(ans)
    ans = solution.suggestedProducts(products=["havana"], searchWord="tatiana")
    print(ans)
