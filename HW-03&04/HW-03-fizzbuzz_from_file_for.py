#Написать fizzbuzz для 20 троек чисел, 
#которые записаны в файл. Читаете из файла первую строку, 
#берете из нее числа, считаете для них fizzbuzz, выводите.


file = open ('FB.txt', 'r')
for i in file:
    number = list(map(int, i.split()))
    fizz = int(number[0])
    buzz = int(number[1])
    c = int(number[2])
    for j in range(1, c+1):
        if j % fizz == 0 and j % buzz == 0:
            print("FB", end=" ") # результат выводим в строку
            continue
        elif j % fizz == 0:
            print("F", end=" ") # результат выводим в строку
            continue
        elif j % buzz == 0:
            print("B", end=" ") # результат выводим в строку
            continue   
        print(j, end=" ") # результат выводим в строку
    print(end='\n') # начинаем новую строку для следующей тройки чисел
file.close()