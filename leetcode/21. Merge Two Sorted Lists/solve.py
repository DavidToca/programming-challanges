# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode()
        
        current = root

        while(l1 or l2):
            if not l1:
                current.next = l2
                return root.next
            elif not l2:
                current.next = l1
                return root.next
            else:
                if(l1.val < l2.val):
                    l3 = l1
                    l1 = l1.next
                else:
                    l3 = l2
                    l2 = l2.next
            
            current.next = ListNode(val=l3.val)
            
            current = current.next

        return root.next