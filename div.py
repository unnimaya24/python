number = int(input("  Enter a number : "))

if((number % 7 == 0) and (number % 3 == 0)):
    print("Given Number {0} is Divisible by 7 and 3".format(number))
else:
    print("Given Number {0} is Not Divisible by 7 and 3".format(number))