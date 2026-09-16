# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            fast,slow = (head.next).next,head.next
        except:
            return False
        while fast != slow:
            try: 
                fast = fast.next.next
            except:
                return False
            
            slow = slow.next  
        return True
        
    