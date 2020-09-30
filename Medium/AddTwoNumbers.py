# Medium
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Assumptions: Positive Ints. Has Elements. Given in sorted reverse. 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

#For fun solution with pythonic shorthand. 
#def AddTwoNumbers(listOne, listTwo):
    #summedNum = int("".join([str(value1) for value1 in reversed(listOne)])) + int("".join([str(value2) for value2 in reversed(listTwo)]))
    #return [int(x) for x in str(summedNum)][::-1]

#print(AddTwoNumbers([2,4,3],[5,6,4]))

# [value]pointer]->[value]pointer]->
class ListNode(object):
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = None

# Traverse list backwards. Add and carry if divisible by 10. If final value has carry, append the 1 at the end of list.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode)->ListNode:
        # Avoids edge cases when inserting into linked lists
        extraNode = ListNode() 
        curr = extraNode # Position of inserting a new node
        carry = 0

        # Iterate for as long both are not None
        while l1 or l2 or carry:
            #Take node value and sum, hold carry
            p = l1.val if l1 else 0
            q = l2.val if l2 else 0
            s = p + q + carry # need temp to get next two
            carry = s // 10 # // is floor division
            summed = s % 10 # Take single digit after taking carry            

            # Insert digit into list
            curr.next = ListNode(summed)

            # Update Pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return extraNode.next





