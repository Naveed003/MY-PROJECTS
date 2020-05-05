while True:
    num = int(input('enter an integer: '))
    if num > 0:
        tnum = num
        reverse = 0
        while tnum > 0:
            digit = tnum % 10
            tnum = tnum//10
            reverse = reverse*10 + digit
        print(reverse)
    else:
        print('negative numbers cannot be reversed')
    print('='*36)
