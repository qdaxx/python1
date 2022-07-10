def print_numbers(limit):
    for i in range(limit):
        print(i)

n = int(input("n = "))
print_numbers(n)

def privet():
    print("Привет")

privet()

def add_numbers(a, b):
    return a + b
print(add_numbers(10,10) - add_numbers(3,7))

def func(x):
    if x<0:
        return x ** 2
    else:
        return x ** 3

def main():
    for i in range(-3,4):
        y=func(i)
        print('func(', i, ') = ', y, sep='')

main()

def print_info(name='Лимон', color='Жёлтый', price='70-1kg'):
    print('Объект:', name, sep='\t')
    print('Цвет:', color, sep='\t')
    print('Цена:', price, sep='\t')
    print()

print_info('Помидор', 'Красный', '60-1kg')

print_info()
