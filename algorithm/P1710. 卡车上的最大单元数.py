#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-30 22:30:16
LastEditTime: 2022-01-30 22:33:25
Description:
FilePath: 1710.卡车上的最大单元数.py
"""

from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda el: el[1], reverse=True)
        count = 0
        for box in boxTypes:
            if truckSize > box[0]:
                count += box[0] * box[1]
                truckSize -= box[0]
            else:
                count += truckSize * box[1]
                break
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.maximumUnits(
        boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10))
