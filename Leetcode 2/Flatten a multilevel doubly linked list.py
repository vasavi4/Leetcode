class Solution:
    def child(self,node,bottom,next):
        curr=bottom
        while curr.next:
            if curr.child:
                self.child(curr,curr.child,curr.next)
            curr=curr.next
        node.next=bottom
        bottom.prev=node
        node.child=None
        curr.next=next
        if next:
            next.prev=curr
        
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]': 
        temp=head
        while temp:
            if temp.child:
                next=temp.next
                self.child(temp,temp.child,next)
            temp=temp.next
        return head
