while True:
    str = input('enter the sentence/word: ')
    l = len(str)
    for i in range(l):
        print(str[i], '\t', str[-i-1])
