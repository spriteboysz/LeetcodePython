#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 22:28
FileName: LCP
Description:LCR 142. 训练计划 IV.py 
"""
from typing import Optional

from common.ListNode import ListNode


class Solution:
    def trainningPlan(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        elif not l2:
            return l1
        nodes = []
        while l1:
            nodes.append(l1)
            l1 = l1.next
        while l2:
            nodes.append(l2)
            l2 = l2.next
        nodes.sort(key=lambda node: node.val)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    print(Solution().trainningPlan(ListNode.create("[1,2,4]"), ListNode.create("[1,3,4]")))
