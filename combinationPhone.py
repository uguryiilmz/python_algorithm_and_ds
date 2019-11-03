# digits='2'

# digits_set= {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
# digits_length=[]
# output=[]

# for i in digits:
#     digits_length.append(digits_set[i])
    
# if(len(digits)==1):
#     for i in range(len(digits_length)):
#         for j in digits_length[i]:
#             output.append(j)
#     print(output)
# else:
#     for i in range(len(digits_length)):
#         for j in digits_length[i]:
#             for k in range(i+1,len(digits_length)):
#                 for z in digits_length[k]:
#                     comb=j+z
#                     output.append(comb)

#     print(output)
# 
# digits='23' 
# dict_set = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz","10":" "}
# result = [""]
# for digit in digits:
#     lst = dict_set[digit]
#     newresult = []
#     for char in lst:
#         for str in result:
#             newresult.append(str+char)
#     result = newresult
# print(result)

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
    p                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []
        if digits:
            backtrack("", digits)
        return output


obj=Solution()
obj.letterCombinations('23')


