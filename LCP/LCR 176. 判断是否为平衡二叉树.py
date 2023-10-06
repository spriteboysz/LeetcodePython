#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-04 00:16
FileName: LCP
Description:LCR 176. 判断是否为平衡二叉树.py 
"""
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root):
            if not root:
                return 0
            return max(depth(root.left), depth(root.right)) + 1

        if not root:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(
            depth(root.left) - depth(root.right)) <= 1


if __name__ == '__main__':
    print(Solution().isBalanced(TreeNode.create("[3,9,20,null,null,15,7]")))
