#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-04-06 22:10:22
LastEditTime: 2022-04-06 22:32:18
Description: 
FilePath: 109.有序链表转换二叉搜索树.py
'''
#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def maketree(nums):
            if not nums:
                return
            index = (len(nums) - 1) // 2
            node = TreeNode(nums[index])
            node.left = maketree(nums[:index])
            node.right = maketree(nums[index + 1 :])
            return node

        if not head:
            return head
        values = []
        while head:
            values.append(head.val)
            head = head.next

        root = maketree(values)
        return root


# @lc code=end
