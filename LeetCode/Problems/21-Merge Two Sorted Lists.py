class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode() 
        tail=head
        
        while list1 and list2:
            if list2.val<list1.val:
                tail.next=list2
                list2=list2.next         
            else:
                tail.next=list1
                list1=list1.next
            tail=tail.next
            
        if list1:
            tail.next=list1
        elif list2:
            tail.next=list2
            
        return head.next