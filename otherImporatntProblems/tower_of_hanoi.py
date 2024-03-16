def TOH(n,beg,aux,end):
    if n==1:
        print("move the disk",beg,'to',end)
    else:
        TOH(n-1,beg,end,aux)
        print("move the disk",beg,'to',end)
        TOH(n-1,aux,beg,end)
a=4
TOH(a,'B','A','E')

#another method
# def TOH(n,beg,aux,end):
#     global count
#     if n==1:
#         print("move the disk",beg,'to',end)
#         count+=1
#         return
#     else:
#         TOH(n-1,beg,end,aux)
#         count+=1
#         print("move the disk",beg,'to',end)
#         TOH(n-1,aux,beg,end)
# a=int(input("Enter the number of disk:"))
# count=0
# TOH(a,'B','A','E')
