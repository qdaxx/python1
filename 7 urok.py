response = ""
while response != "Выйти":
    response = input("Напишите 'Выйти' чтобы выйти: ")

print()
n=1
while n <= 10:
    print("n=", n)
    n+=1

a=0
while a<=0:
    a=int(input("Введите положительное число: "))
print("Вы ввели", a)

while True:
    print("Напишите 123 чтобы выйти из цикла")
    resp=input(">")
    if resp == "123":
        break
print("Цикл остановлен")


name = None
while True:
    print("Menu:")
    print("1 - Enter your name")
    print("2 - Print greeting")
    print("3 - Quit")
    responsee = input("Choose an action")
    print()
    if responsee == "1":
        name = input("Enter your name:")
    elif responsee == "2":
        if name:
            print("Hello, ", name,"!",sep="")
        else:
            print("I dont know your name")
    elif responsee == "3":
        break
    else:
        print("Incorrect input")

d=0
while d<10:
    d+=1
    if d==7:
        continue
    print(d)

attempts = 3
while attempts > 0:
    attempts -=1
    password = input("Введите пароль: "
                     "(осталось {} попыток)".format(attempts+1))
    if password == "123":
        print("Вход разрешен")
        break
else:
    print("Вход запрещён")

print()
for i in range(10):
    print(i)
    if i==5:
        break

print()
for i in range(7):
    for j in range(15):
        print("*", end="")
    print()
