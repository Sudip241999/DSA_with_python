def quick(lst,l,h):
    piv=l
    lt=l+1
    rt=h
    
    while True:
        while lst[piv] <= lst[rt] and lt<= rt:
            rt=rt-1
            if lt>rt:
                return piv
        if lst[piv] > lst[rt]:
            lst[piv],lst[rt]=lst[rt],lst[piv]
            piv = rt
            rt = rt-1
        while lst[piv] >= lst[rt] and lt <= rt:
                lt=lt+1
        if lt > rt:
            return piv
        if lst[piv] < lst[lt]:
            lst[piv],lst[lt]=lst[lt],lst[piv]
            piv=lt
            lt=lt+1

def quicksort(lst1,l,h):
    if l < h:
        piv = quick(lst1,l,h)
        quicksort(lst1,l,piv-1)
        quicksort(lst1,piv+1,h)
lst1 =[2,4,8,1,6]
print("unsorted list  :  ", lst1)
piv=quicksort(lst1,0,len(lst1)-1)
print("sorted list  :   ",lst1)