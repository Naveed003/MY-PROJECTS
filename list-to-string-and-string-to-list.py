while True:
    l = eval(input('enter the list(if empty input[])'))
    s = str(input("enter the string(if empty enter ' ')"))
    lenlist = len(l)
    lenstr = len(s)


    def listtostring():
        str1 = ''
        for i in range(lenlist):
            a = str(l[i])
            str1 = str1 + str(l[i])
        print(str1)


    def stringtolist():
        for i in range(lenstr):
            a = s[i]
            l.append(a)
        print(l)


    if l == []:
        stringtolist()

    else:
        listtostring()
    print('='*50)

