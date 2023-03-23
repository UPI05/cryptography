import math

def encryption(p, k):
    res = ""
    vigtb = create_vignere_table()
    for i in range(min(len(p), len(k))):
        if ord(p[i]) < ord('A') or ord(p[i]) > ord('Z'):
            res += p[i] 
            continue
        res += vigtb[ord(k[i]) - ord('A')][ord(p[i]) - ord('A')] 
    return res
    
def decryption(c, k):
    res = ""
    vigtb = create_vignere_table()
    for i in range(min(len(c), len(k))):
        if ord(c[i]) < ord('A') or ord(c[i]) > ord('Z'):
            res += c[i] 
            continue
        for j in range(26):
            if vigtb[ord(k[i]) - ord('A')][j] == c[i]:
                res += chr(ord('A') + j)
                break
    return res

def create_vignere_table():
    vignere_table = [['A' for i in range(51)] for j in range(51)]
    for i in range(51):
        for j in range(i + 1):
            vignere_table[j][i - j] = chr(ord('A') + (i % 26))
    return vignere_table

def repeat_key(t, k):
    key = ""
    key_with_spaces = ""
    for i in range(math.ceil(len(t) / len(k))):
        key += k 
    cnt = 0
    for x in t:
        if ord(x) < ord('A') or ord(x) > ord('Z'):
            key_with_spaces += x 
        else:
            key_with_spaces += key[cnt]
            cnt += 1
    return key_with_spaces



ip = input('Nhap 0 de ma hoa, 1 de giai ma:')

if ip == '0':
    p = input('Nhap ban ro: ')
    k = input('Nhap key: ')

    p = p.upper()
    k = repeat_key(p, k.upper().replace(' ', ''))

    c = encryption(p, k)

    print(c)

else:
    c = input('Nhap ban ma: ')
    k = input('Nhap key: ')

    c = c.upper()
    k = repeat_key(c, k.upper().replace(' ', ''))

    p = decryption(c, k)

    print(p)
