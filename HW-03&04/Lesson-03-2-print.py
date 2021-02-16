#Каждый пишет сумму списка при помощи for и while
L = [3, 5, 1]

sum  = 0
index = 0
list_last_index = len(L)
while (index < list_last_index):
	sum += L[index]
	index += 1   
print(sum)