while True:
    num = int(input('enter a integer to check: '))
    if num < 1:
        print(num, 'is not a prime number')
    else:
        for i in range(2, num):
            if num % i == 0:
                print(num, 'Is not a prime number')
                break
        else:
            print(num, 'Is a prime number')
        print('='*27)
