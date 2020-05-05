num1 = int(input('enter number 1: '))
num2 = int(input('enter number 2: '))
num3 = int(input('enter number 3: '))
if num1 == num2 == num3:
    print('all numbers are equal')
else:
    if num1 > num2:
        if num1 > num3:
            greatest = num1
        else:
            greatest = num3
    else:
        if num2 > num3:
            greatest = num2
        else:
            greatest = num3
    print('greatest is', greatest)
