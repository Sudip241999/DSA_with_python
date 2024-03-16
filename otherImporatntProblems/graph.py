class graph:
    def __init__(self,row,col):
        self.matrix=[]
        self.row=row
        self.column=col
    def createMatrix(self):
        for i in range(self.row):   
            a = []
            for j in range(self.column):  
                a.append(0)
            self.matrix.append(a)
        
    def display(self):
        for i in range(self.row):
            for j in range(self.column):
                print(self.matrix[i][j], end=" ")
            print()
        print(self.matrix)
    def adjacencyMatrix(self,list):
        k=0
        for i in list:
            self.matrix[i[0]][i[1]]=1
    def outDegree(self):
        out_degree_list=[]
        for i in self.matrix:
            k=0
            for j in i:
                k=k+j
            out_degree_list.append(k)
        print(out_degree_list)
    def indegree(self):
        indegreee=[]
        k=0
        for i in self.matrix:
            for j in range(self.column):
                k=k+i[0]
            indegreee.append(k)
        print(indegreee)




l=[[0,1],[0,2],[1,2],[1,3],[2,4],[3,5],[4,5]]
ob=graph(6,6)
ob.createMatrix()
ob.display()
ob.adjacencyMatrix(l)
print()
ob.display()
ob.indegree()










