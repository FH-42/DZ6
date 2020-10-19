text = open('Praktika 6.3', 'r')

for word in text.readlines():
    b = word.strip('\n').split(';')
    a = sum(map(int, b[0].split()))
    c = a // len(b[0].split())
    d = a % len(b[0].split())
    e = []
    f = list(map(int, b[1].split()))
    e += c, d
    # f = map(int(), b[1].split())
    # print(e)
    if e == f:
        print('True')
    else:
        print('False')




