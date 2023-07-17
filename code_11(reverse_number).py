num = int(input('enter num:'))
reverse = 0
n = num
while n != 0:
    reverse = (reverse*10) + n % 10
    n //= 10

print(f'reverse of {num} is {reverse}')