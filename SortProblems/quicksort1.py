def partition(a,l,h):
    pivot=a[l]
    low=l+1
    high=h
    while(low<high):
        while(a[low]<=pivot):
            low+=1
        while a[high]>pivot:
            high-=1
        if low<high:
            a[low],a[high]=a[high],a[low]
    a[l],a[high]=a[high],a[l]
    return high
def quicksort(a,l,h):
    if(l<h):
        partitionInd = partition(a,l,h)
        quicksort(a,l,partitionInd)
        quicksort(a,partitionInd+1,h)

l=[2,4,8,1,6]
quicksort(l,0,4)
print(l)