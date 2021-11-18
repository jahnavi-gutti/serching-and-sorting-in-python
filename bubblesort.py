def bubblesort(a):
    for i in range(0,len(a)-1):
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
a=[7,3,8,1,2,6,3,9]
print(bubblesort(a))
    
        
