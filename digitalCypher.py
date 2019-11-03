# import string
# alphabets=list(string.ascii_lowercase)

# message='looktoeye'
# code=[13, 17, 16, 11, 24, 19, 6, 27, 6]
# output=[]

# dict={}
# message_array=[]
# for i in range(len(alphabets)):
#   dict[alphabets[i]]=i+1

# for i in range(len(message)):
#   if message[i] in dict:
#     message_array.append(dict[message[i]])

# for i in range(len(code)):
#   output.append(code[i]-message_array[i])

# #print(message_array)

# print(output)


# j=1
# i=0
# string_out=" "
# while(j<len(output)):
#   if output[i]==output[j] and j!=len(output)-1 and output[:j]==output[j:j+j]:
#           for k in range(j):
#             string_out+=str(output[k])
#           print(int(string_out))
#           break  
#   elif output[i]==output[j] and j==len(output)-1:
#         for k in range(j):
#           string_out+=str(output[k])
#         print(int(string_out))
#         break  

#   j+=1


def find_the_key(message, code):
  key = "".join(str(code[i] + 96 - ord(char)) for i, char in enumerate(message))
  l = len(key)
  for i in range(1, l + 1):
      if (key[:i] * l)[:l] == key:
          return int(key[:i])

print(find_the_key('scout',[20 ,12 ,18 ,30 ,21]))