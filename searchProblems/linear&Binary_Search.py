class create_list:
	def __init__(self,l):
		self.list=l
	def display(self):
		print(self.list)
	def linear_search(self,item):
		i=0
		while i<len(self.list):
			if item==self.list[i]:
				print("The position:",i)
				break
			i+=1
		if i==len(self.list):
			return-1
	def binary_search(self,n):
		l=0
		h=len(self.list)
		while l<h:
			mid=(l+h)//2
			if n==self.list[mid]:
				return mid
			elif n<self.list[mid]:
				h=mid-1
			else:
				l=mid+1
		if l>=h:
				return - 1
l=[1,6,8,5]
item=2
ob=create_list(l)
ob.display()
#ob.linear_search(item)
print(ob.binary_search(item))            
