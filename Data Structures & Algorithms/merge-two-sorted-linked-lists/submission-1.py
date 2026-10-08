# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1

        c1 = list1
        c2 = list2
        res = []
        # init the result 
        if c1.val < c2.val:
            res.append(c1)
            c1 = c1.next
        else:
            res.append(c2)
            c2 = c2.next
        
        while c1 != None and c2 != None:
            if c1.val < c2.val:
                res[-1].next = c1
                res.append(c1)
                c1 = c1.next
            else:
                res[-1].next = c2
                res.append(c2)
                c2 = c2.next

        # put the rest nodes into result
        if c1 == None:
            while c2 != None:
                res[-1].next = c2
                res.append(c2)
                c2 = c2.next
        elif c2 == None:
            while c1 != None:
                res[-1].next = c1
                res.append(c1)
                c1 = c1.next 
        return res[0]