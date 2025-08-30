from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"({self.val} -> {self.next})"


# iterative, 2 pointers way
def reverseList_(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    while curr:
        (curr.next, prev, curr) = (prev, curr, curr.next)
    return prev


# recursive approach
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:

    if not head:
        print("end of recusion; returning with None")
        return None

    if not head.next:
        return head

    newHead = reverseList(head.next)
    print(f"head: {head}, returned: {newHead}")
    head.next.next = head
    head.next = None

    return newHead


def reverse_linked_list_recursive(head):
    if head is None:  # handles empty linked list
        return head

    if head.next is None:  # handles linked list with one node
        return head

    # A. label the end node as the new head node
    print(f"before: {head.next}")
    new_head = reverse_linked_list_recursive(head.next)
    print(f"after: {new_head}")

    # B. set the new head node's next_node to be the previous
    #    head node (which is now the end node)
    head.next.next = head

    # C. set the old head node's next_node to None,
    #    which makes it the end node
    head.next = None

    return new_head


if __name__ == '__main__':
    lst = ListNode(1, ListNode(2, ListNode(3)))
    print(reverseList(lst))
