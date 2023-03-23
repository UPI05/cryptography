c = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
c_bytes = bytes.fromhex(c)

x = [i for i in c_bytes]
print(x)

res = []

res.append(c_bytes[0] ^ ord('m'))
res.append(c_bytes[1] ^ ord('y'))
res.append(c_bytes[2] ^ ord('X'))
res.append(c_bytes[3] ^ ord('O'))
res.append(c_bytes[4] ^ ord('R'))
res.append(c_bytes[5] ^ ord('k'))
res.append(c_bytes[6] ^ ord('e'))
res.append(c_bytes[7] ^ ord('y'))
res.append(c_bytes[8] ^ ord('2'))


print(bytes(res))
