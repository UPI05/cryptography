inp = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
inp_bytes = bytes.fromhex(inp)

for i in range(256):
    out = []
    for j in inp_bytes:
        out.append(j ^ i)
    print(bytes(out))
