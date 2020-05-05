while True:
    number = int(input('total numbers of rows(less than 10): '))
    for num in range(1, number+1):
        for i in range(num):
            print(num, end=" ")
        print("\n")
    print('='*45)
