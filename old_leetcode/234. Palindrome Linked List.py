

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


def test(f):
    h = ListNode(1, ListNode(2, ListNode(3)))
    print(h)


@test
def is_palindrome(head: ListNode | None):
    pass
