#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-14 22:32:54
LastEditTime: 2022-01-14 22:54:04
Description: 
FilePath: 203.移除链表元素.py
'''
#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        current = head
        while head:
            if head.val == val:
                current = head.next
                head = head.next
            else:
                break
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return current


# @lc code=end
