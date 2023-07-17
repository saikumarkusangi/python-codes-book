# The string is same after reversing of it is called as Palindrome

s = input('enter an string:')
reverse = ''
for i in range(len(s)-1,-1,-1):
    reverse += s[i]
if s == reverse:
    print('palindrome')
else:
    print('not a palindrome')
