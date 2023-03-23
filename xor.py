p = 'label'
for x in p:
    print(chr(ord(x) ^ 13), end='')
