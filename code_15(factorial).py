num = int(input('enter num:'))
sum = 1
for i in range(1,num+1):
    sum *= i
print(f'factorial of {num} is {sum}')