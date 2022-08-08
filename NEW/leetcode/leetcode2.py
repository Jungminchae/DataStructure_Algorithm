#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = [l1.val]
        l2_list = [l2.val]
        
        while l1.next:
            l1 = l1.next
            l1_list.append(l1.val)
        
        while l2.next:
            l2 = l2.next
            l2_list.append(l2.val)
            
        
        l1_list.reverse()
        l2_list.reverse()
        
        l1_list = list(map(str, l1_list))
        l2_list = list(map(str, l2_list))
        
        l1_int = int("".join(l1_list))
        l2_int = int("".join(l2_list))
        
        result = str(l1_int + l2_int)
        result = list(map(lambda x: x, result))
        
        result.reverse()
        head = ListNode(result.pop(0))
        
        def add(data):
            node = head
            while node.next:
                node = node.next
            node.next = ListNode(data)
        
        while result:
            val = result.pop(0)
            add(val)
            
        return head