#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 22:19
FileName: LCP
Description:LCR 077. 排序链表.py 
"""
from common.ListNode import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        nodes.sort(key=lambda el: el.val)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    print(Solution().sortList(ListNode.create("[4,2,1,3]")))
