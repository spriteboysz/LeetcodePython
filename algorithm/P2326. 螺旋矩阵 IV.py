#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-03 12:05
FileName: algorithm
Description:P2326. 螺旋矩阵 IV.py 
"""
from typing import Optional, List

from common.ListNode import ListNode


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = [[-1 for _ in range(n)] for _ in range(m)]
        left, right, top, bottom = 0, n - 1, 0, m - 1
        while head:
            for j in range(left, right + 1):
                if head:
                    grid[top][j] = head.val
                    head = head.next
            top += 1
            for i in range(top, bottom + 1):
                if head:
                    grid[i][right] = head.val
                    head = head.next
            right -= 1
            for j in range(right, left - 1, -1):
                if head:
                    grid[bottom][j] = head.val
                    head = head.next
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                if head:
                    grid[i][left] = head.val
                    head = head.next
            left += 1
        return grid


if __name__ == '__main__':
    head = ListNode.create(data='[3,0,2,6,8,1,7,9,4,2,5,5,0]')
    print(Solution().spiralMatrix(m=3, n=5, head=head))
    head = ListNode.create(data='[0,1,2]')
    print(Solution().spiralMatrix(m=1, n=4, head=head))
