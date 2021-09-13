n = int(input('\nType a number, and its factorial will be printed: '))
if n < 0:
    print('You must enter a non negative integer')
fact = 1
for i in range(2, n + 1):
    fact = fact * i
print('\nFactorial of',n,'is',fact)
