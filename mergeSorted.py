def merge(nums1,m,nums2,n):
        i=m-1
        j=n-1
        p=len(nums1)-1
        
        while i>0 and j>=0:
            if nums1[i]<=nums2[j]:
                nums1[p]=nums2[j]
                j-=1
                p-=1
            else:
                nums1[p]=nums1[i]
                i-=1
                p-=1
        return nums1
            

print(merge([1,2,3,0,0,0],3,[2,5,6],3))
    

arr=[1,2,3,5]

print(arr[1:3])