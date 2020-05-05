# armstrong numbers
while True:
    number = int(input('enter the number to check: '))
    num = number
    result = 0
    totaldigit = len(str(number))
    if number == 0:
        print('0 is not a armstrong number')
    else:
        while number != 0:
            digit = number % 10
            result += digit**totaldigit
            number //= 10
        print('\n')
        if num == result:
            print(num, 'is an armstrong number')
        else:
            print(num, 'is not an armstrong number')
    print('='*35)
