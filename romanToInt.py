def romanInt(s):
    romans={'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}
            
    sum=0
    for i in range(len(s)-1):
        if romans[s[i]]<romans[s[i+1]]:
            sum-=romans[s[i]]
        else:
            sum+=romans[s[i]]
                
    sum+=romans[s[-1]]
            
    return sum



print(romanInt('III'))
            