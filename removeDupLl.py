class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        dummy=head
        while(head!=None and head.next):
            if (head.val==head.next.val):
                head.next=head.next.next
            head=head.next
        return dummy
        

list=ListNode(1)
list.next=ListNode(1)
list.next.next=ListNode(2)
list.next.next.next=ListNode(3)
list.next.next.next.next=ListNode(3)

sol=Solution()
sol.deleteDuplicates(list)