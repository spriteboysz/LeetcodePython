#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-09-26 23:00
FileName: algorithm
Description:P2816. 翻倍以链表形式表示的数字.py 
"""
from typing import Optional

from common.ListNode import ListNode


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val > 4:
            head = ListNode(0, head)
        cur = head
        while cur:
            cur.val = cur.val * 2 % 10
            if cur.next and cur.next.val > 4:
                cur.val += 1
            cur = cur.next
        return head


if __name__ == '__main__':
    print(Solution().doubleIt(ListNode.create("[9,9,8]")))
