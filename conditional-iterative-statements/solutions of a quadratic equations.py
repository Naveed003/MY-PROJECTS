print('ax^2+bx+c=0')
# taking input of coeificiant of x
a = int(input('enter the value of a: '))
b = int(input('enter the value of b: '))
c = int(input('enter the value of c: '))

# finding discriminant

d = (b**2)-(4*a*c)

if d < 1:
    print('roots are imaginary')
else:
    solution1 = (-b+((d)**(1/2)))/(2*a)
    solution2 = (-b-((d)**(1/2)))/(2*a)
    print('roots of the quadratic equations are (', solution1, ',', solution2, ')')
