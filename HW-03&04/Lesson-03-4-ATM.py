#Банкомат выдает сумму максимально возможными купюрами
amount = int (input("Please enter the amount you want to withdraw: "))
banknots = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

while amount>0:
	for i in range(0,len(banknots)):
            if amount>=banknots[i]:
                print(banknots[i]," , ",int(amount/banknots[i])," Banknots Requires")
                amount=amount%banknots[i];
