#import numpy as np
#import matplotlib.pyplot as plt

f = open('task3-ciphertext.txt', 'r').read()
#print(f)
freq = [0 for i in range(26)]

for x in f:
    if ord(x) - ord('a') < 0 or ord(x) - ord('a') >= 26:
        continue
    freq[ord(x) - ord('a')] += 1

#plt.plot(np.array(freq))
#plt.show()

sorted_freq = [(freq[i], chr(i + ord('a'))) for i in range(26)]
sorted_freq.sort(key=lambda a: a[0])

#for x in sorted_freq[::-1]:
#    print(x[1], end = ': ')
#    print(x[0])

target_freq = ['e', 't', 'a', 'o', 'n', 's', 'i', 'r', 'h', 'l', 'd', 'c', 'm', 'u', 'w', 'b', 'f', 'g', 'p', 'y', 'v', 'k', 'x', 'q', 'j', 'z']

saved_positions = []

for i in range(26):
    for j in range(len(f)):
        if j in saved_positions:
            continue
        if f[j] == sorted_freq[::-1][i][1]:
            f = "".join([f[:j], target_freq[i], f[j + 1:]])
            saved_positions.append(j)

print(f)

