p1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
p2 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
k1k2k3 = []

for i in range (0, len(p1)):
    k1k2k3.append(p1[i] ^ p2[i])

p3 = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

bk123 = bytes(k1k2k3)

flag = []

for i in range (0, len(p3)):
    flag.append(p3[i] ^ bk123[i])

print(bytes(flag))

