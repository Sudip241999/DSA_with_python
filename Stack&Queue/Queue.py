# class queue:
#     def __init__(self):
#         self.front=None
#         self.rear=None
#     def enqueue(self,value):
#         if self.front==None:
#             self.front=value
#             self.rear=value
#         else:
#             p=self.rear
#             self.rear=value
#     def dequeue(self):
#         if self.front==None and self.rear==None:
#             print("queue is empty")
#         elif self.front==self.rear:
#             q=self.front
#             item=q.info
#             del q
#             self.front=None
#             self.rear=None
#             return item
#         else:
#             p=self.front
#             item=p.info
#             self.front=p.link
#             del p
#             return item
#     def display(self):
#         temp=self.front
#         while temp!=self.rear:
#             print(temp.info)
#             temp=temp.link
#         print(temp.info)
# ob=queue()
# ob.enqueue(30)
# ob.enqueue(50)
# ob.dequeue()
# ob.display()


class LinearQueue:
    def __init__(self):
        self.size=10
        self.list=[0 for i in range(self.size)]
        
        self.front=-1
        self.rear=-1
    def enqueue(self,item):
        if self.rear==self.size-1:
            print("queue is full")
            return       
        self.rear+=1
        # print('rear is: ',self.rear)       
        self.list[self.rear]=item
        if self.front==-1:
            self.front=0
            # print("front is :",self.front)
    def dequeue(self):        
        if self.front==-1 and self.rear==-1:
            print("queue is empty")           
            return
        item=self.list[self.front]
        if self.front==self.rear:
                self.front=-1
                self.rear=-1
        else:
              
                self.front+=1
                print("front is : ",self.front)         
        return item
    def display(self):
        if self.front==-1 and self.rear==-1:
             print("queue is empty")
             return
        for i in range(self.front,self.rear+1):
             print(self.list[i],end=" ")

ob=LinearQueue()
ob.enqueue(50)
ob.enqueue(40)
ob.display()
ob.dequeue()
ob.display()