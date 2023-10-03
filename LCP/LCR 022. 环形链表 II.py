#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-01 23:35
FileName: LCP
Description:LCR 022. 环形链表 II.py 
"""
from common.ListNode import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        nodes = set()
        while head:
            if head in nodes:
                return head
            nodes.add(head)
            head = head.next


if __name__ == '__main__':
    print(Solution().detectCycle(ListNode.create("[3,2,0,-4]")))
