# Node Class for a linked List
# [value]next ptr]->
class Node:
    # Basic linked list node structure
    def __init__(self,val):
        self.val = val
        self.next = None

    # Visit each node in the linked list
    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next
    
    # Remove Duplicates in the list
    def remove_duplicates(self):
        uniques = []            
        node = self             
        previous = None
        # If node value in list, set prev ptr to next node
        # If node value not in list, add
        while node != None:     
            if node.val in uniques: 
                previous.next = node.next # make previous point to cur next, cur node cut
            else:
                uniques.append(node.val) # Add to unique values list
            previous = node  # Set previous to current
            node = node.next # Set current to next, increments while loop
    
    # Find the kth element from the right of the linked list
    def find_kth_to_last(self,k):
        if k < 0: return None    #Edge case, no nodes
        ptr1, ptr2 = self, self
        i = -1
        # Finds node, then finds null
        while ptr1 != None:
            ptr1 = ptr1.next     
            if i < k: 
                i += 1
            else: 
                ptr2 = ptr2.next # Move with ptr1 till ptr1 hits null
        if i == k: 
            return ptr2.val
        else: 
            return None
    
    def delete_node(self):
        node = self
        if node == None or node.next == None:
            return False
        node.val = node.next.val
        node.next = node.next.next
        return True

