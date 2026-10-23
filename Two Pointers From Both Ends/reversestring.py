def reversestring(str):
    str=list(str)
    left=0
    right=len(str)-1
    while left<right:
        str[left],str[right]=str[right],str[left]
        left+=1
        right-=1
    return "".join(str)

str1="hello"
print(reversestring(str1))
str2="name"
print(reversestring(str2))

"""
The method used two pointer method to reverse a string, 
First it is converted to list
two pointer will swap until they reach middle of the string
Odd or even string, it works fine
O(log n) time complexity, because it covers half the distance
"""