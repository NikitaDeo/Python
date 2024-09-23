class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to serve as the start of the merged list
        dummy = ListNode()
        current = dummy
        
        # Iterate through both lists while both are non-empty
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach the remaining part of the non-empty list (if any)
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        # Return the merged list, which starts at dummy.next
        return dummy.next

# Helper function to print linked list
def print_linked_list(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    print(values)

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Example usage:
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

sol = Solution()
merged_list = sol.mergeTwoLists(list1, list2)

print_linked_list(merged_list)  # Output: [1, 1, 2, 3, 4, 4]