#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-01 23:38
FileName: LCP
Description:LCR 023. 相交链表.py 
"""
from common.ListNode import ListNode


class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> ListNode:
        seen = set()
        while head1:
            seen.add(head1)
            head1 = head1.next
        while head2:
            if head2 in seen:
                return head2
            head2 = head2.next


if __name__ == '__main__':
    print(Solution().getIntersectionNode(ListNode.create("[1,2,3]"), ListNode.create("[4,5,6]")))
