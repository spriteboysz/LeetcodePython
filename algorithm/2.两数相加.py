#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-16 00:07:56
LastEditTime: 2022-03-02 22:53:42
Description: 
FilePath: 2.两数相加.py
"""
#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = cur = ListNode()
        carry = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            carry, mod = divmod(a + b + carry, 10)
            cur.next = ListNode(mod)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            cur = cur.next
        if carry:
            cur.next = ListNode(carry)
        return l3.next


# @lc code=end
