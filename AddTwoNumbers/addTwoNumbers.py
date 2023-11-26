#Add Two Numbers
#time complexity -  O(max(N, M)) where N and M are the lengths of the input linked lists l1 and l2, respectively.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry

        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry > 0:
        current.next = ListNode(carry)

    return dummy.next

def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head

    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()  # Move to the next line after printing the linked list

def print_linked_list_reverse(head):
    if head is None:
        return
    print_linked_list_reverse(head.next)
    print(head.val, end=" ")

if __name__ == "__main__":
    # Test input: l1 = [2,4,3], l2 = [5,6,4]
    l1_arr = [6, 5, 7]
    l2_arr = [9, 5, 4]

    # Create linked lists dynamically
    l1 = create_linked_list(l1_arr)
    l2 = create_linked_list(l2_arr)

    result = addTwoNumbers(l1, l2)
    print("Output:")
    print_linked_list(result)

    # After obtaining the result from addTwoNumbers function
    # Print the resulting linked list in reverse order
    print("Result in Reverse Order:")
    print_linked_list_reverse(result)
