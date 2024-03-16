class node:
    def __init__(self,value):
        self.info=value
        self.link=None
class CircularLinkedList:
    def __init__(self):
        self.start=None
    def insert_at_beginning(self,value):
        n=node(value)
        if self.start==None:
            self.start=n
            n.link=self.start
        else:
            p=self.start
            self.start=n
            n.link=p
            s=p
            while p.link!=s:
                p=p.link
            p.link=self.start
    def insert_at_end(self,value):
        t=node(value)
        temp=self.start
        s=temp
        while temp.link!=s:
            temp=temp.link
        temp.link=t
        t.link=s
    def delete_start(self):
        temp=self.start
        self.start=temp.link
        s=temp
        while temp.link!=s:
            temp=temp.link
        temp.link=self.start
        del s
    def delete_end(self):
        temp=self.start
        s=temp
        while temp.link!=s:
            previous=temp
            temp=temp.link
        previous.link=s
        item=temp.info
        del temp
        return item
    def display(self):
        temp=self.start
        while temp.link!=self.start:

            print(temp.info,end=" ")
            temp=temp.link
        print(temp.info)
    def insert_at_specified_pos(self,value,pos):
        n=node(value)
        temp=self.start
        i=1
        while i!=pos-1:
            previous=temp
            temp=temp.link
            i+=1
        n.link=temp.link
        temp.link=n
    def insert_after_specified_item(self,item,value):
        temp=self.start
        n=node(value)
        while temp.link!=self.start and temp.info!=item:
            
            temp=temp.link
        n.link=temp.link
        temp.link=n
      
    
ob=CircularLinkedList()
ob.insert_at_beginning(50)
ob.insert_at_beginning(40)
ob.insert_at_beginning(20)
ob.insert_at_specified_pos(88,2)
ob.insert_at_specified_pos(122,4)
# ob.insert_after_specified_item(88,122)
ob.display()
        