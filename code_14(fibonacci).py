def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
num = int(input('enter an number:'))

if num <= 0:
    print('enter positive number')
else:
    print(f'fibonacci series of {num}',end=' ')
    for i in range(num):
        print(fibonacci(i),end=',')