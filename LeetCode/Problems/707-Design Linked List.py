class Node(object):
    def __init__(self, val=0,nxt=None,prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def get(self, index: int) -> int:
        if index>=self.length:
            return -1
        i=0
        nd=self.head
        while(i!=index):
            nd=nd.next
            i+=1
        return nd.val
        

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head=Node(val)
            self.tail=self.head
            self.length=1
        else:
            self.head.prev=Node(val,self.head)
            self.head=self.head.prev
            self.length+=1
        
    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head=Node(val)
            self.tail=self.head
            self.length=1
        else:
            self.tail.next=Node(val,prev=self.tail)
            self.tail=self.tail.next
            self.length+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.length:
            return
        if index==0:
            return self.addAtHead(val)
        if index==self.length:
            return self.addAtTail(val)
        i=0
        nd=self.head
        while(i!=index):
            nd=nd.next
            i+=1
        newnode=Node(val,nd,nd.prev)
        nd.prev.next=newnode
        nd.prev=newnode
        self.length+=1

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.length:
            return
        if self.length==1:
            self.head=None
            self.tail=None
            self.length=0
            return
        if index==0:
            self.head=self.head.next
            self.head.prev=None
            self.length-=1
            return
        if index==self.length-1:
            self.tail=self.tail.prev
            self.tail.next=None
            self.length-=1
            return
        i=0
        nd=self.head
        while(i!=index):
            nd=nd.next
            i+=1
        nd.prev.next=nd.next
        nd.next.prev=nd.prev
        self.length-=1