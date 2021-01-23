import random 
# Заготовка для первого предложения
def loe_fail(f):
    fail=open(f,'r') # ну ошибка и ошибка, чего бубнить то
    mas=[] 
    for rida in fail:
        mas.append(rida.strip(";\n"))
    fail.close()
    return mas
first = loe_fail("first_file.txt")
second1 = loe_fail("second1_file.txt")
second2 = loe_fail("second2_file.txt")
third = loe_fail("third_file.txt")
# Спрашиваем у пользователя про его знак (буду брать данные у пользователя, через Combobox и/или messagebox у tkinter)
zodiac = int(input("Введите число с номером знака зодиака: "))
# Если число введено верно — выдаём гороскоп 
goroskop=((random.choice(first))+" "+(random.choice(second1))+" "+(random.choice(second2))+" "+(random.choice(third)))
print(goroskop)