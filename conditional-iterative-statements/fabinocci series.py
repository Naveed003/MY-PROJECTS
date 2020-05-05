n = int(input('enter the of term: '))
a1 = 0
a2 = 1
for i in range(n):
    print(a1)
    a3 = a1
    a1 = a2
    a2 += a3
