#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-05 15:52:05
LastEditTime: 2022-04-05 15:56:31
Description: 
FilePath: 328.奇偶链表.py
"""
from common.ListNode import ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        nodes = nodes[::2] + nodes[1::2]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.oddEvenList(ListNode.create("[2,1,3,5,6,4,7]")))
