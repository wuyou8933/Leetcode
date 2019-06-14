class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        head = l3
        while l1!= None and l2!=None:
            if l1.val<l2.val:
                l3.next = l1
                l1=l1.next
            else:
                l3.next = l2
                l2=l2.next
            l3=l3.next
            
        if l1 != None:
            l3.next = l1
            
        if l2 !=None:
            l3.next = l2
                
        return head.next