num = int(input())
flag = True
for i in range(2,num):
    if num % i == 0:
        flag = False
        break
if flag:
      print(f'{num} is a prime')
else:
      print(f'{num} is not a prime')