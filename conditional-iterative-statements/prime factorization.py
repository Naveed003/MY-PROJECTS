import numpy as np
n = int(input("Enter the Number: "))
list = []
arr1 = np.load('primenumbers.npy')
for i in arr1:
    while n % i == 0:
        n /= i
        print(n)
        list.append(i)
        print(list)
    print(i)
    if i > n/2:
        list.append(n)
        break
    if n == 1:
        break
n = int(n)
for i in range(999983, n+1):
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
    while n % i == 0:
        n /= i
        print(n)
        list.append(i)
        print(list)

    if i > n/2:
        list.append(n)
        break
    if n == 1:
        break
print(list)
