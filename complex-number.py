while True:
    print('z = a+ib')
    a = int(input('enter value of real part(a): '))
    b = int(input('enter the value of imaginary part(b)'))
    print('z=', a, '+', b, 'i')
    magnitude_z = ((a**2)+(b**2))**(1/2)
    r = magnitude_z
    print('magnitude of z is', r)
    print('polar form: ', r, '(', a, '/', r, '+ i', b, '/', r)
    print('conjugate form: ', a+(-b*'i'))
    print('='*45)
