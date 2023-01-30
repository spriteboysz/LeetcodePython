#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/29 22:21
FileName: algorithm/P2511. 最多可以摧毁的敌人城堡数目.py
Description: 
"""
from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        last, ans, cnt = 0, 0, 0  # last的初值只要不是1或-1就可以
        for fort in forts:
            if fort:  # 遇到非0值，找到子数组的端点
                if not fort + last:  # 合法的端点只能是1或-1，如果两个端点的值加起来为0就是合法的
                    ans = max(ans, cnt)
                last = fort
                cnt = 0
            else:  # 遇到0，当前计数+1
                cnt += 1
        return ans


if __name__ == '__main__':
    print(Solution().captureForts(forts=[1, 0, 0, -1, 0, 0, 0, 0, 1]))
