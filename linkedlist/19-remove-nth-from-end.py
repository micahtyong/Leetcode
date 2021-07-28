# Idea: Make rule, move it, then prune


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def findLengthOfLinkedList(self, head):
        i = 0
        while head: 
            i += 1
            head = head.next
        return i
    
    # 1 pass, O(1) space
    def removeNthFromEnd(self, head, n):
        sentinel = ListNode(0, head)
        start = end = sentinel
        # create ruler
        for i in range(n + 1):
            end = end.next
        # move ruler
        while end: 
            end = end.next
            start = start.next
        # prune first elem of ruler
        start.next = start.next.next
        return sentinel.next
        
        
    # 2 passes
    def removeNthFromEndAlt(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = self.findLengthOfLinkedList(head)
        new_n = length - n - 1 
        if (new_n == -1): 
            head = head.next
            return head
        sentinel = head
        while new_n > 0: 
            sentinel = sentinel.next
            new_n -= 1
        sentinel.next = sentinel.next.next 
        return head
    
    
    