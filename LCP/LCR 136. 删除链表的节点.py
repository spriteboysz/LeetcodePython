#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 22:10
FileName: LCP
Description:LCR 136. 删除链表的节点.py 
"""
from common.ListNode import ListNode


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1, head)
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


if __name__ == '__main__':
    print(Solution().deleteNode(ListNode.create("[4,5,1,9]"), 5))
