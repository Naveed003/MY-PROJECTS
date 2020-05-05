while True:
    num = int(input('enter the number: '))
    factorial = 1
    if num < 1:
        print('factorial does not exist for -ve numbers')
    elif num == 0:
        print('factorial of 0 is 1')
    else:
        for i in range(1, num+1):
            factorial *= i
        print('The factorial of', num, 'is', factorial)
    print('='*50)
