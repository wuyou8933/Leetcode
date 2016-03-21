class Solution(object):
    def rotateRight(self, head, k):
        """
            :type head: ListNode
            :type k: int
            :rtype: ListNode
            """
        if head==None:
            return head
        if k==0:
            return head
        tail=head
        n=1
        while tail.next:
            tail=tail.next
            n+=1
        tail.next=head
        for i in range(n-k%n):
            tail=tail.next
        head=tail.next
        tail.next=None
        return head