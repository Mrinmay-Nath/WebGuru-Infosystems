'''Write a program using a match statement to implement a menu. The user should input a
number (1 to 4) corresponding to the following actions:
1. Add
2. Subtract
3. Multiply
4. Divide
Print the chosen operation based on the user’s input. If the input is not between 1
and 4, print "Invalid Choice"'''

num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
choice=int(input("1.Add \n2.Subtract\n3.Multiply\n4.Divide\nEnter the choice: "))
match choice:
    case 1:
        print("The addition is",num1+num2)
    case 2:
        print("The Subtraction is",num1-num2)
    case 3:
        print("The Multiplication is",num1*num2)
    case 4:
        print("The Divition is",num1/num2)
    case _:
        print("Invalid Choice")