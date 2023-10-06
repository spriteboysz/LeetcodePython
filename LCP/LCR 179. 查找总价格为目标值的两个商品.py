#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-04 00:05
FileName: LCP
Description:LCR 179. 查找总价格为目标值的两个商品.py 
"""
from typing import List


class Solution:
    def twoSum(self, price: List[int], target: int) -> List[int]:
        left, right = 0, len(price) - 1
        while left < right:
            if price[left] + price[right] < target:
                left += 1
            elif price[left] + price[right] > target:
                right -= 1
            else:
                return [price[left], price[right]]


if __name__ == '__main__':
    print(Solution().twoSum(price=[3, 9, 12, 15], target=18))
