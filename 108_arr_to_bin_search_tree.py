# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode(0)
        
        def feed (root,arr):
            if len(arr) == 0:return
            mid = len(arr)//2
            root.val = arr[mid]
            
            
            if len(arr[:mid]) >0:
                root.left = TreeNode()
                feed(root.left, arr[:mid])
            if len(arr[mid+1:]) >0:   
                root.right = TreeNode()
                feed(root.right, arr[mid+1:])
        
        feed(root,nums)
        return root
            