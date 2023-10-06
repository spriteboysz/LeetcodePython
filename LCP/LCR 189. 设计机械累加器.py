#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 23:41
FileName: LCP
Description:LCR 189. 设计机械累加器.py 
"""


class Solution:
    def mechanicalAccumulator(self, target: int) -> int:
        if target == 1:
            return 1
        return target + self.mechanicalAccumulator(target - 1)


if __name__ == '__main__':
    print(Solution().mechanicalAccumulator(5))
    print(Solution().mechanicalAccumulator(7))
