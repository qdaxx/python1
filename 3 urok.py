int_list = [1, 2, 3, 5]
char_list = ['a', 'b', 'c']
empty_list = []
print(len(char_list))
print('a' in char_list)
print(int_list)

print(char_list[0]+char_list[2])

result = int_list[0]+int_list[3]
print(result)

print(char_list)
print(empty_list)
list_from_range = list(range(10))
print(list_from_range)

list_from_string = list("привет!")
print(list_from_string)
print(list_from_string[0])
print(list_from_string[3])
index = int(input("Введите индекс"))
element = list_from_string[index]
print(element)

my_list = [1, 2, 3, 4, 5, 6, 7]
sub_list = my_list[:-1:2]
print(sub_list)
print(my_list[2:-2])

print(my_list[::-2])
print(8 in my_list)
print(len(my_list))
v=int(input("Введите число"))
if v in my_list:
    print("Число в списке")
else:
    print("Число не в списке")

print("при" in "привет")

b = []
b.append(3)
b.append(5)
b.append(b[0]+b[1])
print(b)
del b[1]
print(b)
a = [5, 10, 30, 60]
a[3] = 22
print(a)

c = [1, 2, 3, 4, 5, 6, 7,]
for x in c:
    print("{} ^ 2 = {}".format(x, x ** 2))

n=10
fibs = [1, 1]
for i in range(n-2):
    fibs.append(fibs[i] + fibs[i+1])
print(fibs)
