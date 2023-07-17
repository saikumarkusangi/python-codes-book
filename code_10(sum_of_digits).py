num = int(input('enter number:'))
sum = 0
n = num
while n != 0:
  sum += n%10
  n //= 10
print(f'sum of {num} is {sum}')