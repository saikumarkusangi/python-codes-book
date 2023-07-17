num1 = int(input('enter from:'))
num2 = int(input('enter to:'))
sum = 0
for i in range(num1,num2+1):
    sum += i
print(f'sum of numbers from {num1} to {num2} is {sum}')