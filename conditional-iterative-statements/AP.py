while True:
    print('='*42)
    import math
    # taking input of first term,last term,c.d
    a = int(input('enter the first term of AP: '))
    l = int(input('enter the last term of AP: '))
    d = int(input("enter the common difference: "))

    if (l > a and d > 0) or (l < a and d < 0):
        for AP in range(a, l+1, d):
            print(AP, end=',')

        print("\n ========================= \n what do u whant to find  \n option 1 : nth term \n option 2 : sum of first n terms \n ========================= ")

        # option selection

        option = int(input('option: '))
        if option == 1:
            t_terms = int(((l-a)/d)+1)
            print('total number of terms is', t_terms)
            print('n is nth term')
            n = int(input('enter n value(less than total numbers):'))
            an = a+(n-1)*d
            print("nth term with given n value is", an)

        elif option == 2:
            print('n is sum of first n terms')
            n = float(input('enter the n value'))
            x = int(2*(a) + (n-1)*d)
            y = n*(x)
            z = y/2
            print('sum of first n terms is', z)

        else:
            print('invalid input')
    else:
        print('invalid input')
    print('='*42)
