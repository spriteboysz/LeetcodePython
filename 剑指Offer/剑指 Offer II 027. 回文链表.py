#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-16 23:02:53
LastEditTime: 2022-05-16 23:04:16
Description:
FilePath: 剑指 Offer II 027. 回文链表.py
"""
# ! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-16 23:02:53
LastEditTime: 2022-05-16 23:02:54
Description: 
FilePath: 剑指 Offer II 027. 回文链表.py
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values == values[::-1]
