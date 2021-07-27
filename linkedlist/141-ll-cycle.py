# Idea: set() representing what we've seen so far

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # O(1) space, O(n) time
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try: 
            tortoise, hare = head, head.next.next
            hare = tortoise.next.next
            while tortoise != hare:
                tortoise, hare = tortoise.next, hare.next.next
            return True
        except:
            return False

    # O(n) space, O(n) time
    def hasCycleEasy(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pos = set()
        while head:
            if head in pos:
                return True
            pos.add(head)
            head = head.next
        return False