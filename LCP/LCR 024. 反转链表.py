#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-01 23:42
FileName: LCP
Description:LCR 024. 反转链表.py 
"""
from common.ListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].next = nodes[i - 1]
        nodes[0].next = None
        return nodes[-1]


if __name__ == '__main__':
    print(Solution().reverseList(ListNode.create("[1,2,3,4,5]")))
