class stack:
    def __init__(self):
        self.list=[]
        self.size=10
        self.top=-1
    def push(self,item):
        if self.top==self.size-1:
            print("stack is full")
            
        else:
            self.top+=1
            self.list.append(item)

    def pop(self):
        if self.top==-1:
            print("stack is empty")
        else:
            item1=self.list[self.top]
            
            self.list.pop(self.top)
            self.top-=1
            return item1
    def peek(self):
        if self.list!=[]:
            return self.list[self.top]
        else :
            return 
    def display(self):
        print(self.list)
            

ob=stack()
ob.push(10)  
# print(ob.pop()) 
ob.push(40)  
ob.push(60)  
ob.push(20)        
# print(ob.peek())
print(ob.pop())
ob.display()
        
        