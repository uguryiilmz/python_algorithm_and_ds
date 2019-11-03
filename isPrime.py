class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n<2:
            return 0
        
        
        sum=0
        isPrime=[0]*n
        isPrime[0]=1
        isPrime[1]=1
        
        for i in range(2,int(n**0.5)+1):
            if isPrime[i]==0:
                for j in range(2,n,1):
                    if i*j<n:
                        isPrime[i*j]=1
                    else:
                        break
                        
        return sum(isPrime)