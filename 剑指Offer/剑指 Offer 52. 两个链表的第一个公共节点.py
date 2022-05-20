#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-05-20 22:22:07
LastEditTime: 2022-05-20 22:22:08
Description: 
FilePath: 剑指 Offer 52. 两个链表的第一个公共节点.py
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        pointA, pointB = headA, headB
        while pointA != pointB:
            pointA = pointA.next if pointA else headB
            pointB = pointB.next if pointB else headA
        return pointA
