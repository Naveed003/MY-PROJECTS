while True:
    num1 = int(input('enter the first number: '))
    num2 = int(input('enter the second number: '))
    x = abs(num1)
    y = abs(num2)
    if x > y:
        greatest = x
    else:
        greatest = y
    while True:
        if greatest % x == 0 and greatest % y == 0:
            lcm = greatest
            print('lcm of', num1, 'and', num2, 'is', lcm)
            break
        greatest += 1
    print('='*25)
