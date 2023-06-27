#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-26 22:16:02
LastEditTime: 2022-03-26 22:18:51
Description: 
FilePath: 206.反转链表.py
"""


#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack, h = [], head
        while h:
            stack.append(h)
            h = h.next

        reverse = ListNode()
        h = reverse
        while stack:
            node = stack.pop()
            node.next = None
            h.next = node
            h = h.next
        return reverse.next

# @lc code=end
