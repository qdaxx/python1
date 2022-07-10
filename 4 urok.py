a = int(input())
b = int(input())
if a > b:
    print("True")
else:
    print("False")

c = float(input())
if c > 0:
    d = c ** 0.5
else:
    d = c ** 2
print(d)

name = (input("Введи своё имя"))
print("Твоё имя:",name)
if name == "Иван":
    print("О,ты мой тёзка")
else:
    print("А меня зовут Иван")

x = int(input())
if 10 < x < 101:
    y = 2 * x - 30
    if y < 0:
        print("Y<0,Y =",y)
    elif y > 0:
        print("Y>0,Y =",y)
    else:
        print("Y=0")

print("""Меню
1 - Уроки
2 - Игра
3 - Сон
""")
a = input("Что ты будешь делать ")
if a == "1":
    print("Ты любишь учиться")
elif a == "2":
    print("Игры тоже хорошо")
elif a == "3":
    print("Сон это полезно")
else:
    print("Нет такого выбора")

l = True
msg = "Yes" if l else"No"
print(msg)

string = input()
if string:
    print(format(string))