#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-14 21:49:00
LastEditTime: 2022-01-14 22:43:47
Description: 
FilePath: 83.删除排序链表中的重复元素.py
'''
#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return head


# @lc code=end
