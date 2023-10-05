#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 22:33
FileName: LCP
Description:LCR 078. 合并 K 个升序链表.py 
"""
from typing import List

from common.ListNode import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode | None:
        if not lists:
            return None
        nodes = []
        for head in lists:
            cur = head
            while cur:
                nodes.append(cur)
                cur = cur.next
        if not nodes:
            return None
        nodes.sort(key=lambda node: node.val)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


if __name__ == '__main__':
    list1 = ListNode.create("[1,4,5]")
    list2 = ListNode.create("[1,3,4]")
    list3 = ListNode.create("[2,6]")
    print(Solution().mergeKLists([list1, list2, list3]))
