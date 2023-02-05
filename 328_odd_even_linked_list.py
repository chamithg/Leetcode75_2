# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = ListNode()
        runner = head
        runner2 = even
        count = 0
        if not head:
            return None
        if not head.next:
            return head
        while runner and runner.next:
            if runner.next and count%2 == 0:
                runner2.next = ListNode(runner.next.val)
                runner2 = runner2.next
                if runner.next.next:runner.next = runner.next.next
                else: runner.next = None
            if runner.next:runner = runner.next
        count +=1
        runner.next = even.next


        return head