# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m = n-1
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length +=1
        
        # we need to remove node length-m
        # first traverse to length-n
        # save temp as length- n . next . next
        # make node.next =. temp
        # return head
        count = 1
        curr = head
        while count < (length - n):
            curr = curr.next
            count +=1
        if n == length:
            return head.next
        
        temp = curr.next.next
        curr.next = temp
        return head


        