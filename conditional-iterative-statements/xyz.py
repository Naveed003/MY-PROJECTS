import numpy as np
a = np.load('primenumbers.npy')
count = 0
for i in a:
    count += 1
print(count)
