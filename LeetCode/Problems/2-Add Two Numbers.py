class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=0
        i=0
        while l1!=None:
            n1+=l1.val*10**i
            l1=l1.next
            i+=1
        n2=0
        i=0
        while l2!=None:
            n2+=l2.val*10**i
            l2=l2.next
            i+=1
        sum=str(n1+n2)
        res=ListNode(val=int(sum[0]))
        for i in sum[1:]:
            res=ListNode(int(i),res)
        return res
        