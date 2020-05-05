while True:
    num = int(input('enter the  number to check: '))
    if num % 2 == 0:
        print(num, 'is even and its is square is', num**2)
    else:
        print(num, 'is odd and its cube is', num**3)
    print('='*20)
