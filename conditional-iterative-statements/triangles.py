import math
while True:
    a = float(input('enter first side  value: '))
    b = float(input('enter second side value: '))
    c = float(input('enter third side value: '))
    if a < 0 or b < 0 or c < 0:
        print("sides of a triangle can't be negative")
    else:
        if a+b > c and b+c > a and a+c > b:
            print('It is a triangle')
            base = float(input('enter base value: '))
            if a == b and b == c and a == c:
                print('it is a equilateral triangle')
            elif a == b or b == c or c == a:
                print('it is a isosceles')
            elif (a**2)+(b**2) == (c**2)or(b**2)+(c**2) == (a**2)or(a**2)+(c**2) == (b**2):
                print('it is a right angle triangle')
                if (a > b):
                    if a > c:
                        largest = a
                    else:
                        largest = c

                else:
                    if b > c:
                        largest = b
                    else:
                        largest = c

                print('hypotenuse is side with value: ', largest)
                if base == a and largest == b:
                    vertical = c
                    print('value of vertical is', vertical)
                elif base == a and largest == c:
                    vertical = b
                    print('value of vertical is', vertical)
                elif base == b and largest == c:
                    vertical = a
                    print('value of vertical is', vertical)
                elif base == b and largest == a:
                    vertical = c
                    print('value of vertical is', vertical)
                elif base == c and largest == a:
                    vertical = b
                    print('value of vertical is', vertical)
                elif base == c and largest == b:
                    vertical = a
                    print('value of vertical is', vertical)
                else:
                    vertical = float(input('enter vertical value: '))
                    base = float(input('enter base value: '))
                print('which sides oppsite angles TRIGONOMETERIC RATIOS u want to find')
                print('option 1: vertical \noption 2: base')
                option2 = int(input("option : "))
                if option2 == 1:
                    sine = vertical/largest
                    cos = base/largest
                    tan = vertical/base
                    cot = base/vertical
                    sec = largest/base
                    cosec = largest/vertical
                    print('sine is', vertical, '/', largest, 'or', sine)
                    print('cos is', base, '/', largest, 'or', cos)
                    print('tan is', vertical, '/', base, 'or', tan)
                    print('cot is', base, '/', vertical, 'or', cot)
                    print('sec is', largest, '/', base, 'or', sec)
                    print('cosec is', largest, '/', vertical, 'or', cosec)

                else:
                    cos = vertical / largest
                    sine = base / largest
                    cot = vertical / base
                    tan = base / vertical
                    cosec = largest / base
                    sec = largest / vertical
                    print('sine is', base, '/', largest, 'or', sine)
                    print('cos is', vertical, '/', largest, 'or', cos)
                    print('tan is', base, '/', vertical, 'or', tan)
                    print('cot is', vertical, '/', base, 'or', cot)
                    print('sec is', largest, '/', vertical, 'or', sec)
                    print('cosec is', largest, '/', base, 'or', cosec)

            else:
                print('it is a scalen triangle')
            p = a+b+c
            s = p/2
            x = (s*(s-a)*(s-b)*(s-c))
            area = x**(1/2)
            height = (area*2)/base
            radius = a*b*c/((a+b+c)*(b+c-a)*(c+a-b)*(a+b-c))**(1/2)
            print('area is', area)
            print('perimeter is', p)
            print('semi perimeter is', s)
            print('height is', height)
            print('radius of the triangle is', radius)

        else:
            print('not a triangle')
        print('='*65)
