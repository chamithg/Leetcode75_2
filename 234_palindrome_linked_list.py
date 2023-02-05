# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        runner = head
        element_arr = []
        while runner:
            element_arr.append(runner.val)
            runner = runner.next
        
        left,right = 0, len(element_arr)-1

        print(element_arr)

        while element_arr[left] == element_arr[right] and right > left:
            left +=1
            right -=1

        if right - left <2 and element_arr[left] == element_arr[right]:
            return True
        else: return False