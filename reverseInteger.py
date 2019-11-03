def reverse(x):
    # long rev=0
    # isNegative=False
    # if x<0:
    #     isNegative=True
    #     x=x*-1
    # while(x!=0):
    #     rev=rev*10+x%10
    #     x=x//10
    # if rev>INTEGER.max or rev<INTEGER.min:
    #     return
    
    # if isNegative:
    #     return -rev
    # else:
    #     return rev

    rev=0
    prevRev=0
    isNegative=False
    if x<0:
        isNegative=True
        x=x*-1
    while (x!=0):
        rev=rev*10+x%10
        if((rev-x%10)/10!=prevRev):
            return 0
        prevRev=rev
        x=x/10
    return rev
    

    
print(reverse(1534236469))