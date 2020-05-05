while True:
    str = input('enter the sentence/word: ')
    str2 = input('enter the letter: ')
    l = len(str)
    count = 0
    for i in range(l):
        if str[i] == str2:
            count += 1
        else:
            continue
    print(count)
    5
