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
            print(self.list)
    def pop(self):
        if self.top==-1:
            print("stack is empty")
        else:
            item1=self.list[self.top]
            
            self.list.pop(self.top)
            self.top-=1
            return item1
# string="4 13 5 / +"
list=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
ob=stack()

for i in list:

    if i in ("+","-","*","/"):
        item1=ob.pop()
        item2=ob.pop()
        print("item1: ",item1)
        ob.push(str(int(eval(item2+i+item1))))
    else:
        ob.push(i)
