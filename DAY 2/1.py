'''Write a program to check if a number is even or odd. If the number is even, print "Even
Number". If it’s odd, print "Odd Number".Also add another condition to check if the
number is zero.'''


num=int(input("Enter the number : "))
if num==0:
    print("The number is Zero")
elif num%2==0:
    print("The number is Even")
else:
    print("The number is Odd")
    