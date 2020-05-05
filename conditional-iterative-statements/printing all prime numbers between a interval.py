while True:
    lower_limit = int(input('enter lower limit: '))
    upper_limit = int(input('enter upper limit '))
    l=[]
    for i in range(lower_limit, upper_limit+1):
        if i > 1:
            for a in range(2, i):
                if i % a == 0:
                    break
            else:
                l.append(i)
                print(i)
    print(l)
    print('='*27)
