class node:
    def __init__(self,value):
        self.info=value
        self.link=None
class Slink:
    def __init__(self):

        self.start=None
    def insert_at_beginning(self,value):
        n1=node(value)
        n1.link=self.start
        self.start=n1
    def inser_at_end(self,value):
        t=node(value)
        temp=self.start
        while temp.link!=None:
            temp=temp.link
        temp.link=t
    def delete_at_start(self):
        temp=self.start
        self.start=temp.link
        item=temp.info
        del temp
        return item
    def delete_last_node(self):
        temp=self.start
        while temp.link!=None:
            previous=temp
            temp=temp.link
        item=temp.info
        del temp
        previous.link=None
        return item
    def display(self):
        temp=self.start
        while temp!=None:

            print(temp.info,end=" ")
            temp=temp.link
    def insert_at_specified_pos(self,value,pos):
        i=1
        t=node(value)
        temp=self.start
        while i== pos-1:
            previous=temp
            temp=temp.link
            i+=1
        previous.link=t
        t.link=temp
    def insert_after_specified_item(self,value,item):
        temp=self.start
        n=node(value)
        while temp.link!=None and temp.info!=item:
            
            temp=temp.link
        n.link=temp.link
        temp.link=n
    def delete_at_specified_pos(self,pos):
        temp=self.start
        i=1
        
        while i!=pos-1:
            previous=temp
            temp=temp.link
            i+=1
        item=temp.info
        previous.link=temp
        # del temp
        return item
    def reverseLinkedList(self):
        c=None
        n=self.start
        while n!=None:
            t=n.link
            n.link=c
            c=n
            n=t
        self.start=c



ob=Slink()
ob.insert_at_beginning(90)
ob.insert_at_beginning(60)
ob.insert_at_beginning(30)
ob.insert_at_beginning(40)
ob.insert_at_specified_pos(75,2)
ob.insert_after_specified_item(55,40)
ob.display()
print()
ob.reverseLinkedList()
ob.display()
