#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-02 23:24:02
LastEditTime: 2022-04-02 23:24:22
Description: 
FilePath: 86.分隔链表.py
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head

        cur, nodes, bigger = head, [], []
        while cur:
            if cur.val < x:
                nodes.append(cur)
            else:
                bigger.append(cur)
            cur = cur.next
        nodes.extend(bigger)

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]
