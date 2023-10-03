#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-01 23:26
FileName: LCP
Description:LCR 021. 删除链表的倒数第 N 个结点.py 
"""
from common.ListNode import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1, head)
        fast, slow = dummy, dummy
        while n:
            fast = fast.next
            n -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


if __name__ == '__main__':
    print(Solution().removeNthFromEnd(ListNode.create("[1,2,3,4,5]"), 2))
