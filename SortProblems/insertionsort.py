def insertionsort(list):
    for i in range(1,len(list)):
        k=list[i]
        j=i-1
        while j>=0 and k<list[j]:
            list[j+1]=list[j]
            j=j-1
        list[j+1]=k
lst=[23,45,6,7,8,9]
insertionsort(lst)
print(lst)