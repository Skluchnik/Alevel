#Написать fizzbuzz для 20 троек чисел, 
#которые записаны в файл. Читаете из файла первую строку, 
#берете из нее числа, считаете для них fizzbuzz, выводите.


file = open ('FB.txt', 'r')
file2 = open ('New_file.txt', 'w')
for i in file:
    number = list(map(int, i.split()))
    fizz = int(number[0])
    buzz = int(number[1])
    c = int(number[2])
    for j in range(1, c+1):
        if j % fizz == 0 and j % buzz == 0:
            file2.write("FB")
            continue
        elif j % fizz == 0:
            file2.write("F")
            continue
        elif j % buzz == 0:
            file2.write("B")
            continue   
        file2.write(str(j))
    file2.write('\n')
file2.close()