# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pointer = head
        if pointer is None:
            return None
        else:
            while pointer.next is not None:
                if pointer.val == pointer.next.val:
                    pointer.next = pointer.next.next
                else:
                    pointer = pointer.next
            return head
