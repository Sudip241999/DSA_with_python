class node:
    def __init__(self,item):
        self.key=item
        self.right=None
        self.left=None
class binarySearchTree:
    def __init__(self):
        self.root=None
    def CreateBST(self,list):
        for item in list:
            n=node(item)
            if self.root==None:
                self.root=n
            else:
                par=None
                temp=self.root
                while temp!=None:
                    if item<temp.key:
                        par=temp
                        temp=temp.left
                    else:
                        par=temp
                        temp=temp.right
                if item<par.key:
                    par.left=n
                else:
                    par.right=n
    def preOrder(self,temp):
        if temp!=None:
            print(temp.key,end=" ")
            self.preOrder(temp.left)
            self.preOrder(temp.right)
    def inOrder(self,temp):
        if temp!=None:
            self.inOrder(temp.left)
            print(temp.key,end=" ")
            self.inOrder(temp.right)
    def postOrder(self,temp):
        if temp!=None:
            self.postOrder(temp.left)
            self.postOrder(temp.right)
            print(temp.key,end=" ")
    def height(self,temp):
        if temp==None:
            return 0
        else:
            return max(self.height(temp.left),self.height(temp.right))+1
    def search(self,item):
        par=None
        temp=self.root
        while temp!=None:
            if item==temp.key:
                print("found")
                return temp,par
            else:
                if item<temp.key:
                    par=temp
                    temp=temp.left
                else:
                    par=temp
                    temp=temp.right
        print("item not found")
    def delete(self,item):
        temp,par=self.search(item)
        print(temp)
        print(par)
        if temp.left==None and temp.right==None:
            print("no children")
        elif temp.left==None and temp.right!=None:
            print("")
        



l=[100,50,90,130,110,150,120,30,20,45,130,140,115,105]
ob=binarySearchTree()
ob.CreateBST(l)
ob.preOrder(ob.root)
print()
ob.inOrder(ob.root)
print()
ob.postOrder(ob.root)
print()
print(ob.height(ob.root))
print()
# print(ob.search(50))
print()
ob.delete(50)






        