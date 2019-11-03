
    
def climbStairs(n):
    memo=[0]* (n+1)

    def climb_stairs(i,n,memo):
        if i>n:
            return 0
        if i==n:
            return 1
        if memo[i]>0:
            return memo[i]  
        memo[i]=climb_stairs(i+1,n,memo)+climb_stairs(i+2,n,memo)
        return memo[i]

    
    return climb_stairs(0,n,memo)





print(climbStairs(5))