import math

nash_pod = 1
nash_et = 1

num = int(input("Введите номер квартиры"))
et = int(input("Введите количетсво этажей"))
pod = int(input("Введите количество подъездов"))
kv = int(input("Введите количество квартир на єтаже"))

def help (num, et, kv):
    if num <= pod*et*kv:
        nash_pod = 1
        while num > et*kv:
            num -= et*kv
            nash_pod +=1
        nash_et = math.ceil(num/kv)
        return print("Зайти в " + str(nash_pod) + " подъезд, на " + str(nash_et) + "этаж")
    else:
        return print("Неправильный номер")



help(num, kv,et)