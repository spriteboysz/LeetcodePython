#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-16 22:59:02
LastEditTime: 2022-05-16 23:02:05
Description:
FilePath: 剑指 Offer II 024. 反转链表.py
"""
#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-16 22:59:02
LastEditTime: 2022-05-16 22:59:03
Description: 
FilePath: 剑指 Offer II 024. 反转链表.py
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return

        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        nodes.reverse()
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]
