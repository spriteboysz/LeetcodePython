#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-25 22:51
FileName: algorithm/P2487. 从链表中移除节点.py
Description: 
"""
from typing import Optional

from common.ListNode import ListNode


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        nodes1, nodes2 = [], []
        while head:
            nodes1.append(head)
            head = head.next
        nodes2.append(nodes1[-1])
        for i in range(len(nodes1) - 2, -1, -1):
            if nodes1[i].val >= nodes2[-1].val:
                nodes2.append(nodes1[i])

        for i in range(len(nodes2) - 1, 0, -1):
            nodes2[i].next = nodes2[i - 1]
        nodes2[0].next = None
        return nodes2[-1]


if __name__ == '__main__':
    print(Solution().removeNodes(ListNode.create("[5,2,13,3,8]")))
