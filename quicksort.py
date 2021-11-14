def quicksort(a,si,ei):
    if si>=ei:
        return
    pi=partition(a,si,ei)
    quicksort(a,si,pi-1)
    quicksort(a,pi+1,ei)
def partition(a,si,ei):
    pivot=a[si]
    c=0
    for i in range(si,ei+1):
        if a[i]<pivot:
            c+=1
    a[si+c],a[si]=a[si],a[si+c]
    pi=si+c
    i=si
    j=ei
    while i<j:
        if a[i]<pivot:
            i=i+1
        elif a[j]>=pivot:
            j=j-1
        else:
            a[i],a[j]=a[j],a[i]
            i=i+1
            j=j-1
    return pi
a=[10,5,3,1,7,9,4]
quicksort(a,0,len(a)-1)
print(a)
