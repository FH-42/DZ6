a = int(input())

d = []
#f = []
#e = []
if a // 2 == 0:
    print("Введите нечётное число")
if a % 2 and a > 0:
    for c in range(1, a+1, 2):
        d.append(c)
        #d.extend(len(d)[-2::-1])
    d = d + d[len(d)-2::-1]
        #e = list([len((d)[-2::-1])])
        #f = [d + e]
    for y in d:
        space = int((a-y)/2)
        print(' '*space + '*' * y + ' '*space)
