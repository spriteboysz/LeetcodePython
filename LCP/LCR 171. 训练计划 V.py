#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 23:03
FileName: LCP
Description:LCR 171. 训练计划 V.py 
"""
from common.ListNode import ListNode


class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> ListNode:
        visited = set()
        while head1:
            visited.add(head1)
            head1 = head1.next
        while head2:
            if head2 in visited:
                return head2
            head2 = head2.next


if __name__ == '__main__':
    print(Solution().getIntersectionNode(ListNode.create("[4,1,8,4,5]"), ListNode.create("[4,1,8,4,5]")))
