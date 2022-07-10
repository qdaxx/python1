def func():
    """
    Документационная строка(описание функции)
    """
    print("func called")

func()

help(func)

print(func.__doc__)

number = int(input("Введите число"))
print("Двоичная СС", bin(number))
print("Восьмиричная СС", oct(number))
print("Шестнадцатиричная СС", hex(number))

for i in reversed("привет"):
    print(i)

a=int(input())
b=int(input())
c=int(input())
print(min(a,b,c))
print(max(a,b,c))

def func1():
    def func2():
        print("Внутренняя функция")
    print("Внешняя функция")
    func2()

func1()


def funcc():
    global var
    var = "123"
    print(var)
var = "321"
funcc()
print(var)
print()
def loo(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return  result
print(loo(5))

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
for i in range(1, 11):
    print(fib(i))

def hanoi(n, a, b, c):
    if n != 0:
        hanoi(n - 1, a, c, b)
        print("с", a, "на", c)
        hanoi(n-1, b, a, c)
hanoi(3, 'A', 'B', 'C')
