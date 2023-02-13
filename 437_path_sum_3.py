# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0
        def treverse_to_count(root,sum):
            if not root:return
            if sum + root.val == targetSum:
                self.paths +=1
            treverse_to_count(root.left, sum + root.val)
            treverse_to_count(root.right, sum + root.val)

        def treverse(root):
            if not root:return
            treverse_to_count(root,0)
            treverse(root.left)
            treverse(root.right)

        treverse(root)
        return self.paths