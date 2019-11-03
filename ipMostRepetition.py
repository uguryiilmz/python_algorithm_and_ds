ip=['1234567890/tGEF/t24',
'1234567890/tGEF/t24',
'1234567690/tGEF/t24',
'1234567590/tGEF/t24',
'1234567890/tGEF/t24']


dict={}
arr=[]

for i in ip:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

for vals in sorted(dict,key=dict.get,reverse=True):
    print vals, dict[vals]


