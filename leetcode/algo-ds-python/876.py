# 876. Middle of the Linked List
# Easy
# 9.2K
# 269
# Companies
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

# Constraints:

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

# ------------- 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# My solution

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_temp = head
        ct = 1
        while head.next != None:
            head = head.next
            ct += 1
        middle = ct // 2

        for _ in range(middle):
            head_temp = head_temp.next
        return head_temp
    

# Suggested solution === Slow and Fast Pointers:
# Each time, slow go 1 steps while fast go 2 steps.
# When fast arrives at the end, slow will arrive right in the middle.

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow