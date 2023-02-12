# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        left,right = 0,0

        def goright(root,count):
            if not root: return count
            count +=1
            goright(root.right,count)
        
        def goleft(root,count):
            if not root: return count
            count +=1
            goleft(root.right,count)

        if root.left:
            left = goleft(root.left,0)
        if root.right:
            right = goright(root.right,0)

        print(left,right)

