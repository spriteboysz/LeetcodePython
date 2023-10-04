#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 15:38
FileName: LCP
Description:LCR 026. 重排链表.py 
"""
from common.ListNode import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes, cur = [], head
        while cur:
            nodes.append(cur)
            cur = cur.next
        n, nodes2 = len(nodes), []
        for i in range(n // 2 + 1):
            nodes2.append(nodes[i])
            nodes2.append(nodes[n - 1 - i])
        for i in range(n - 1):
            nodes2[i].next = nodes2[i + 1]
        nodes2[n - 1].next = None
        print(head)


if __name__ == '__main__':
    Solution().reorderList(ListNode.create("[1,2,3,4]"))
    Solution().reorderList(ListNode.create("[1,2,3,4,5]"))
