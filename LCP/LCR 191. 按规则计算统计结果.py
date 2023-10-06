#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 23:22
FileName: LCP
Description:LCR 191. 按规则计算统计结果.py 
"""
from collections import Counter
from typing import List


class Solution:
    def statisticalResult(self, arrayA: List[int]) -> List[int]:
        dic = Counter(arrayA)
        if 0 not in dic:
            product = 1
            for num in arrayA:
                product *= num
            for i, num in enumerate(arrayA):
                arrayA[i] = product // num
            return arrayA
        elif dic[0] > 1:
            return [0] * len(arrayA)
        else:
            product = 1
            for num in arrayA:
                if num != 0:
                    product *= num
            for i, num in enumerate(arrayA):
                if num != 0:
                    arrayA[i] = 0
                else:
                    arrayA[i] = product
            return arrayA


if __name__ == '__main__':
    print(Solution().statisticalResult(arrayA=[2, 4, 6, 8, 10]))
