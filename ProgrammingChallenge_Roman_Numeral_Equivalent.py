# 1. For this exercise, start by creating a variable and assigning it a randomly
# generated integer between and inclusive of both 1 and 10.
from random import randint
num = randint(1, 10)

# 2. Then, using your knowledge of if, elif, and else statements, create a
# program which prints the roman numeral equivalent of the randomly generated number.
if num == 10:
    print("The roman numeral equivalent of " + str(num) + " is X")
elif num == 9:
    print("The roman numeral equivalent of " + str(num) + " is IX")
elif num == 8:
    print("The roman numeral equivalent of " + str(num) + " is VIII")
elif num == 7:
    print("The roman numeral equivalent of " + str(num) + " is VII")
elif num == 6:
    print("The roman numeral equivalent of " + str(num) + " is VI")
elif num == 5:
    print("The roman numeral equivalent of " + str(num) + " is V")
elif num == 4:
    print("The roman numeral equivalent of " + str(num) + " is IV")
elif num == 3:
    print("The roman numeral equivalent of " + str(num) + " is III")
elif num == 2:
    print("The roman numeral equivalent of " + str(num) + " is II")
else:
    print("The roman numeral equivalent of " + str(num) + " is I")