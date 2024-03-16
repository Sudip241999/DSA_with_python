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
        previous=None        
        while i!=pos:
            previous=temp
            temp=temp.link
            i+=1
        item=temp.info
        previous.link=temp.link
        del temp
        return item
    def removeNthFromEnd(self, n):

            c=1
            start=self.start
            while start.link!=None:
                start=start.link
                c+=1
            print("length=",c)
            if c==1:
                return None
            else:
                temp=self.start
                prev=None
                i=1
                while i<c-(n-1):
                    prev=temp
                    temp=temp.link
                    i+=1
                prev.link=temp.link

            return self.start

    
    
ob=Slink()
ob.insert_at_beginning(90)
ob.insert_at_beginning(60)
ob.insert_at_beginning(30)
ob.insert_at_beginning(40)
ob.display()
print()
ob.removeNthFromEnd(1)
# ob.insert_at_specified_pos(75,2)
# ob.insert_after_specified_item(55,40)
# print(ob.delete_at_start())
# print(ob.delete_last_node())
ob.display()
# print()
# print(ob.delete_at_specified_pos(2))
# ob.display()



        
        