def maxProduct(list):
    max_prod=0
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if not_common(list[i],list[j]):
                length=len(list[i])*len(list[j])
                max_prod=max(max_prod,length)
    return max_prod

def not_common(s1,s2):
    for i in s1:
        if i in s2:
            return False
    return True

print(maxProduct(["a","aa","aaa","aaaa"]))


        if not head: return None
            prev, cur = None, head

            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev   
        print('cur',cur)
        print('head',head)

