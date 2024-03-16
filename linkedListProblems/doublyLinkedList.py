class node:
    def __init__(self,value):
        self.info=value
        self.prev=None
        self.next=None

class doublyLinkedList:
    def __init__(self):
        self.start=None

    def add_at_the_beginning(self,value):
        n=node(value)
        if self.start==None:
            self.start=n
        else:
            t=self.start
            self.start=n
            t.prev=n            
            n.next=t

    def add_at_the_end(self,value):
        n=node(value)
        if self.start==None:
            self.start=n
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            n.prev=temp    
            temp.next=n

    def delete_from_beginning(self):
        temp=self.start
        item=temp.info
        p=temp.next
        self.start=p
        p.prev=None

    def add_at_the_specific_pos(self,pos,value):
        n=node(value)
        temp=self.start
        i=1
        while i<pos-1:
            temp=temp.next
            i+=1
        k=temp.next
        temp.next=n
        n.prev=temp
        n.next=k
        k.prev=n

    def delete_at_specific_pos(self,pos):
        temp=self.start
        i=1
        while i<pos-1:
            temp=temp.next
            i+=1
        item=temp.next.info
        k=temp.next.next
        temp.next=k
        k.prev=temp
        return item     
    def delete_at_end(self):
        temp=self.start
        while temp.next!=None:
            temp=temp.next
        k=temp.prev
        k.next=None
        item=temp.info
        return item   
    
    def display(self):
        temp=self.start
        while temp!=None:
            print(temp.info,end=" ")
            temp=temp.next
ob=doublyLinkedList()
ob.add_at_the_beginning(20)
ob.add_at_the_beginning(35)
ob.add_at_the_end(45)
ob.add_at_the_end(95)
ob.add_at_the_end(55)
ob.add_at_the_end(435)
ob.delete_from_beginning()
ob.add_at_the_specific_pos(3,88)
ob.display()
ob.delete_at_specific_pos(3)
ob.delete_at_end()
print()
ob.display()
