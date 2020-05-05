while True:
    a = float(input("enter the number: "))
    if a > 00:
        b = str(input("from unit(km,m,cm,mm,ft): "))
        c = str(input("to unit(km,m,cm,mm,ft): "))
        km = "km"
        m = "m"
        cm = "cm"
        mm = "mm"
        ft = "ft"
        if b == km and c == m:
            d = a*1000
        elif b == c:
            d = a
        elif b == km and c == cm:
            d = a*100000
        elif b == km and c == mm:
            d = a*1000000
        elif b == km and c == ft:
            d = a*3280.84
        elif b == m and c == km:
            d = a / 1000
        elif b == m and c == cm:
            d = a*100
        elif b == m and c == mm:
            d = a*1000
        elif b == m and c == ft:
            d = a*3.281
        elif b == cm and c == km:
            d = a/100000
        elif b == cm and c == m:
            d = a/100
        elif b == cm and c == mm:
            d = a*10
        elif b == cm and c == ft:
            d = a/30.48
        elif b == mm and c == km:
            d = a/1000000
        elif b == mm and c == cm:
            d = a/10
        elif b == mm and c == m:
            d = a/1000
        elif b == mm and c == ft:
            d = a/304.8
        elif b == ft and c == km:
            d = a*3280.84
        elif b == ft and c == m:
            d = a/3.281
        elif b == ft and c == cm:
            d = a*30.48
        elif b == ft and c == mm:
            d = a*304.8
        else:
            print("invalid input")
        print(d, c)
        print('='*22)
    else:
        print("negative numbers can't be converted to from one units to another unit")
        print('='*72)
