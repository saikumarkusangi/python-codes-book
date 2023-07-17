# sum of cubes of digits of number is equal to number itself is called armstrong number
num = int(input('enter num:'))
n = num
sum = 0

while n != 0:
    sum += (n%10)**3
    n //= 10

if sum == num:
    print('armstrong number')
else:
    print('not an armstrong number')