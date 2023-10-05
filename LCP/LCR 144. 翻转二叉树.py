#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-04 20:14
FileName: LCP
Description:LCR 144. 翻转二叉树.py 
"""
from common.TreeNode import TreeNode


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode | None:
        if not root:
            return None
        tmp = self.mirrorTree(root.left)
        root.left = self.mirrorTree(root.right)
        root.right = tmp
        return root


if __name__ == '__main__':
    print(Solution().mirrorTree(TreeNode.create("[5,7,9,8,3,2,4]")))
