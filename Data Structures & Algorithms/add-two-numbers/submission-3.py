# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total1 = 0
        k = 1 
        while l1:
            total1 += (l1.val)*k
            k *= 10
            l1 = l1.next
        
        total2 = 0
        x = 1 
        while l2:
            total2 += (l2.val)*x
            x *= 10
            l2 = l2.next
        
        grand =  total1+total2


        # 469
        
        z = ListNode()
        h = z 

        if grand == 0:
            return ListNode(0)


        while grand > 0:
            z.val =  grand%10
            grand = grand//10
            dhdh = ListNode()
            z.next = dhdh
            o = z
            z = z.next
            
        o.next = None
        return h

