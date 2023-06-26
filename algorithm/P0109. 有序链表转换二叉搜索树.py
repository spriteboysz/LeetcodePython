#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-06 22:10:22
LastEditTime: 2022-04-06 22:32:18
Description:
FilePath: 109.有序链表转换二叉搜索树.py
"""
#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
from typing import Optional

from common.ListNode import ListNode
from common.TreeNode import TreeNode


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def create(nums):
            if not nums:
                return
            index = (len(nums) - 1) // 2
            node = TreeNode(nums[index])
            node.left = create(nums[:index])
            node.right = create(nums[index + 1:])
            return node

        if not head:
            return head
        values = []
        while head:
            values.append(head.val)
            head = head.next

        root = create(values)
        return root

# @lc code=end
