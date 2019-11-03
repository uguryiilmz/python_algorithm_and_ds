arr=[2,6,4,8,10,9,15]

l=99
r=-1

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[j]<arr[i]:
            l=min(i,l)
            r=max(j,r)
    
print(r-l+1)

