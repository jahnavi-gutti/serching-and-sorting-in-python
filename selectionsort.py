def selectionsort(a):
    for i in range(len(a)):
        min_idx=i
        for j in range(i+1,len(a)):
            if a[min_idx]>a[j]:
                min_idx=j
        a[i],a[min_idx]=a[min_idx],a[i]
    return a
a=[4,7,2,9,1,5,3]
print(selectionsort(a))

    
