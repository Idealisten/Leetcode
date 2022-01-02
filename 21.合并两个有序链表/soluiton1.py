# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        list3 = ListNode()  # 当前节点
        l3 = list3  # 头节点
        while (list1 is not None and list2 is not None):
            if list1.val < list2.val:
                list3.next = list1
                list3 = list3.next
                list1 = list1.next
            elif list1.val > list2.val:
                list3.next = list2
                list3 = list3.next
                list2 = list2.next
            else:
                list3.next = list1
                list3 = list3.next
                list1 = list1.next
                list3.next = list2
                list3 = list3.next
                list2 = list2.next
        if list1 is None:
            list3.next = list2
        else:
            list3.next = list1
        return l3.next
