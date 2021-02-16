#Задача fizz-buzz.
print ("Введите три целых числа:")
# Вводим исходные значения чисел
a = int(input("первое число (fizz): "))
b = int(input("второе число (buzz): "))
c = int(input("       третье число: "))
#body
for i in range(1, c+1):
    if i % a == 0 and i % b == 0:
        print("FB")
        continue
    elif i % a == 0:
        print("F")
        continue
    elif i % b == 0:
        print("B")
        continue
    print(i)
