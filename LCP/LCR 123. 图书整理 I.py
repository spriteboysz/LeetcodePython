#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 23:08
FileName: LCP
Description:LCR 123. 图书整理 I.py 
"""
from typing import Optional, List

from common.ListNode import ListNode


class Solution:
    def reverseBookList(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return []
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        return nodes[::-1]


if __name__ == '__main__':
    print(Solution().reverseBookList(ListNode.create("[3,6,4,1]")))
