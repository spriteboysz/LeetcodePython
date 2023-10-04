#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 15:53
FileName: LCP
Description:LCR 027. 回文链表.py 
"""
from common.ListNode import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        return nodes == nodes[::-1]


if __name__ == '__main__':
    print(Solution().isPalindrome(ListNode.create("[1,2,3,3,2,1]")))
