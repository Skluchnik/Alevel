#example-1
print ("Give it to me!")
number = int(input())

if (number >= 100):
    print ("Thanks, man!")
elif ((number > 10) and (number < 100)):
    print ("OK :(")
else:
    print ("WHAAAAT????")

if (number > 1000):
    print ("!!!!WOOOOWWWW!!!")

#example-2
>>> x = 5
>>> y = 10
>>> z = 15

>>> (x < y) and (y <= z)
True

>>> x < y <= z
True

#example-3
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> l1 == l2
True
>>> l1 is l2
False
>>> l1 is not l2
True

#example-4
>>> 3 in l1
True
>>> 4 in l1
False
>>> 5 not in l1
True

#example-5
print ($input == 1) ? "One!" : "Not One!";

#example-6
test = True
result = 'Test is True' if test else 'Test is False'
# result = 'Test is True'

#example-7
test = True
print ('ttt' if test else 'fff') # выведет ttt

#example-8
if s !='':
    pass
    
if 8 % 2 != 0:
    pass

#example-9
if s:
    pass
    
if 8 % 2:
    pass

#example-10
a = 11
if a>10 and a < 20:
    pass

#example-11
test = True
result = test and 'Test is True' or 'Test is False'