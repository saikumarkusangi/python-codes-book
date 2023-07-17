# method 1

num1 = int(input('enter num1:'))
num2 = int(input('enter num2:'))
num3 = int(input('enter num3:'))

greatest = max(num1,num2,num3)
print(f'{greatest} is the greatest number')

# method 2

num1 = int(input('enter num1:'))
num2 = int(input('enter num2:'))
num3 = int(input('enter num3:'))
if num1 > num2 and num1 >num3:
    print(f'{num1} is the greatest number')
elif(num2 > num3):
    print(f'{num2} is the greatest number')
else:
    print(f'{num3} is the greatest number')