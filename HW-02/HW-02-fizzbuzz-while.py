#Задача fizz-buzz.
print ("Введите три целых числа:")
# Вводим исходные значения чисел
a = int(input("первое число (fizz): "))
b = int(input("второе число (buzz): "))
c = int(input("       третье число: "))
#body
i = 1
while (i < c):
    if i % a == 0 and i % b == 0:
        print("FB")
    elif i % a == 0:
        print("F")
    elif i % b == 0:
        print("B")
    else:
        print(i)
    i=i+1


