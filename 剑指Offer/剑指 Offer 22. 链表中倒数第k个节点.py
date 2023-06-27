#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-01 00:05:25
LastEditTime: 2022-05-01 00:07:48
Description: 
FilePath: 剑指 Offer 22. 链表中倒数第k个节点.py
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter
