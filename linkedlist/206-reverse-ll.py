# Idea: Sentinel node and new list. 
# Edit: No need for sentinel

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reversedList = None
        while head:
            reversedList = ListNode(head.val, reversedList)
            head = head.next
        return reversedList