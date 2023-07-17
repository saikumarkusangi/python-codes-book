# method 1

num1 = int(input('enter num1:'))
num2 = int(input('enter num2:'))
greatest = max(num1,num2)
print(f'{greatest} is the greatest number')

# method 2

num1 = int(input('enter num1:'))
num2 = int(input('enter num2:'))
if num1 > num2:
    print(f'{num1} is the greatest number')
else:
    print(f'{num2} is the greatest number')