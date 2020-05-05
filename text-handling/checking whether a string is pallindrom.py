while True:
    str = input('enter the word/sentence: ')
    l = len(str)
    str2 = ''
    a = 0
    for i in range(l):
        a = -i-1
        str2 = str2+str[a]
    if str2 == str:
        print('it is a pallindrom')
    else:
        print('not a pallindrom')
