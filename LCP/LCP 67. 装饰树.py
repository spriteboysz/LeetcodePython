#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-25 23:15
FileName: LCP/LCP 67. 装饰树.py
Description: 
"""
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left:
            root.left = TreeNode(-1, left=self.expandBinaryTree(root.left))
        if root.right:
            root.right = TreeNode(-1, right=self.expandBinaryTree(root.right))
        return root


if __name__ == '__main__':
    root = TreeNode.create("[3,1,7,3,8,null,4]")
    solution = Solution().expandBinaryTree(root)
    print(solution)
