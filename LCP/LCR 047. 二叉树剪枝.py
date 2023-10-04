#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 16:38
FileName: LCP
Description:LCR 047. 二叉树剪枝.py 
"""
from common.TreeNode import TreeNode


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode | None:
        if not root:
            return root
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and root.val == 0:
            return None
        return root


if __name__ == '__main__':
    print(Solution().pruneTree(TreeNode.create("[1,null,0,0,1]")))
