n=int(input("Enter a number "))
x= n % 10
print("The last digit in %d = %d" % (n, x))
if((n% 3 == 0) ):
    print("Given Number {0} is Divisible by 3".format(n))
else:
    print("Given Number {0} is Not Divisible by 3 ".format(n))