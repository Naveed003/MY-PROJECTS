import numpy as np
while True:
    arr1 = np.load('primenumbers.npy')
    start = arr1[-1:-2:-1]
    start = (int(start))+1
    upper_limit = arr1[-1]+1000000
    g = int(upper_limit/2)
    for b in range(start, upper_limit+1):

        if b % 2 == 0:
            x = b/2
        else:
            x = (b/2)+0.5
            x = int(x)
        for a in arr1:
            if b % a == 0:
                break

            if a > x:
                arr2 = np.array([b])
                print(b)
                arr3 = np.hstack((arr1, arr2))

                np.save('primenumbers', arr3)

                break

        else:
            for i in range(g, x):
                if i % 2 == 0 and i != 2:
                    continue
                if i % 3 == 0 and i != 3:
                    continue
                if i % 5 == 0 and i != 5:
                    continue
                if i % 7 == 0 and i != 7:
                    continue
                if i % 11 == 0 and i != 11:
                    continue
                if i % 13 == 0 and i != 13:

                    continue
                if i % 17 == 0 and i != 17:
                    continue
                if i % 19 == 0 and i != 19:
                    continue
                if i % 23 == 0 and i != 23:
                    continue
                if x % i == 0:
                    break
            else:
                print(b)
                arr2 = np.array([b])
                arr3 = np.hstack((arr1, arr2))

                np.save('primenumbers', arr3)
    np.save('primenumbers', arr3)
    print('='*50)
