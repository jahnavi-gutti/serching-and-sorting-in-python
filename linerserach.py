def linersearch(a,x):
    for i in range(len(a)):
        if a[i]==x:
            return i
    return -1
a=[3,8,1,7,4,6]
print(linersearch(a,7)+1)
        
        
    
