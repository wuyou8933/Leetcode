class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        head = l3
        p1 = l1
        p2 = l2
        while p1!= None and p2!=None:
            if p1.val<p2.val:
                l3.next = p1
                p1=p1.next
            else:
                l3.next = p2
                p2=p2.next
            l3=l3.next
            
        if p1 != None:
            l3.next = p1
            
        if p2 !=None:
            l3.next = p2
                
        return head.next