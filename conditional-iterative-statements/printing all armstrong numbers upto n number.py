while True:
    print('='*25)
    lower_limit = int(input('enter lower limit: '))
    upper_limit = int(input('enter upper limit '))
    for i in range(lower_limit, upper_limit+1):
        num = i
        result = 0
        totaldigits = len(str(i))
        while (i != 0):
            digit = i % 10
            result = result+digit**totaldigits
            i = i//10
        if num == result:
            print(result)
    print('='*25)
