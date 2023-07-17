num = int(input('enter n:'))
print(f'All prime numbers in range of {num} are',end=' ')
for i in range(2,num+1):
    for j in range(2,i):
        if i % j == 0:
          break
    else:
         print(i,end=',')