#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-05 17:50
LastEditTime: 2022-06-05 17:50
Description:
FilePath: 剑指 Offer II 025. 链表中的两数相加.py
"""


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        carry, node = 0, None
        while s1 or s2 or carry:
            num1 = s1.pop() if s1 else 0
            num2 = s2.pop() if s2 else 0
            carry, num = divmod(num1 + num2 + carry, 10)
            node = ListNode(num, node)
        return node
