while True:
    str = input('enter the word/sentence: ')
    l = len(str)
    c_cap = 0
    c_low = 0
    c_num = 0
    c_a = 0
    c_n = 0
    for i in range(l):
        a = str[i]
        if a.isupper():
            c_cap += 1
        if a.islower():
            c_low += 1
        if a.isalnum():
            c_num += 1
        if a.isalpha():
            c_a += 1

        else:
            c_n += 1

    print('\nThe word/sentence you entered have', c_cap, 'upper case alphabets')
    print('The word/sentence you entered have', c_low, 'lower case alphabets')
    print('The word/sentence you entered have', c_num, 'numbers')
    print('The word/sentence you entered have', c_a, 'alphabets')
    print('The word/sentence you entered have', c_n, 'non alphabets and sentence characters')
