# calculator
while True:
    print("="*34)
    print("option 1= addition")
    print("option 2= subtraction")
    print("option 3= multiplication")
    print("option 4= division")
    print("="*34)

    print("select any option")
    num4 = 'invalid input'
    a = int(input("option :"))
    if a == 1:
        num1 = float(input("enter num1 :"))
        num2 = float(input("enter num2 :"))
        num3 = float(input("enter num3 (if null enter 0) :"))
        num4 = num2+num1+num3
        print("the sum is")
    elif a == 2:
        num1 = float(input("enter num1 :"))
        num2 = float(input("enter num2 :"))
        num3 = float(input("enter num3 (if null enter 0) :"))
        num4 = num1-num2-num3
        print("the difference is")
    elif a == 3:
        num1 = float(input("enter num1 :"))
        num2 = float(input("enter num2 :"))
        num3 = float(input("enter num3 (if null enter 1) :"))
        num4 = num1*num2*num3
        print("the product is")
    elif a == 4:
        num1 = float(input("enter num1 :"))
        num2 = float(input("enter num2 :"))
        num3 = float(input("enter num3 (if null enter 1) :"))
        num4 = num1/num2/num3
        print("the quotient is")
    else:
        print('invalid input')
    print(num4)
    print('='*34)
