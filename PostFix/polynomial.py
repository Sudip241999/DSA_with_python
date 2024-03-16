class term:

	def __init__(self, c,e):
		self.coef=c
		self.exponent=e
		self.link=None

class polynomial:

	def __init__(self):
		self.start=None

	def add_term(self,c,e):

		if self.start==None:
			t=term(c,e)
			self.start=t
			return
		else:
			p=self.start
			while(p!=None and p.exponent!=e):
				prev=p
				p=p.link
			if p!=None:
				p.coef+=c
				return
			if p==None:
				t1=self.start
				prev=None
				while t1!=None and t1.exponent>e:
					prev=t1
					t1=t1.link
				if t1==None:
					tnew=term(c,e)
					prev.link=tnew
				else:
					tnew=term(c,e)
					if prev==None:
						tnew.link=t
						self.start=tnew
					else:
						tnew.link=t1
						prev.link=tnew

	def display(self):
		temp=self.start
		while temp!=None:
			print(temp.coef,"x^",temp.exponent,"+",end=" ")

			temp=temp.link
ob=polynomial()
ob.add_term(6,5)
ob.add_term(5,4)
ob.add_term( 8,3)
ob.add_term(5,2)
ob.display()

						
