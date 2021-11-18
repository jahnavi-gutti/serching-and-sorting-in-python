def insertionsort(a):
        for i in range(1,len(a)):
            key=a[i]
            j=i-1
            while j>=0 and a[j]>key:
                a[j+1]=a[j]
                j=j-1
            a[j+1]=key
        return a

a=[2,7,1,8,2,3,9,4]
print(insertionsort(a))

        
