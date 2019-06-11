class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = None
        
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        if l1.val<l2.val:
            l3 = l1
            l1.next = self.mergeTwoLists(l1.next,l2)
        
        else:
            l3=l2
            l2.next=self.mergeTwoLists(l1,l2.next)
            
        return l3