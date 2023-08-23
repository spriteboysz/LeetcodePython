#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-23 23:29
FileName: algorithm
Description:P2807. 在链表中插入最大公约数.py 
"""
import math
from typing import Optional

from common.ListNode import ListNode


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        while head:
            values.append(head.val)
            values.append(-1)
            head = head.next
        for i in range(1, len(values) - 1, 2):
            values[i] = math.gcd(values[i - 1], values[i + 1])
        # print(values)
        dummy = ListNode(-1)
        cur = dummy
        for i in range(0, len(values) - 1):
            cur.next = ListNode(values[i])
            cur = cur.next
        return dummy.next


if __name__ == '__main__':
    head = ListNode.create("[18,6,10,3]")
    print(Solution().insertGreatestCommonDivisors(head))
