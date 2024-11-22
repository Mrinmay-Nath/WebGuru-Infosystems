'''Write a program using a for loop to print all the numbers from 1 to 50. However:
● If a number is divisible by 3, print "Fizz".
● If it’s divisible by 5, print "Buzz".
● If it’s divisible by both, print "FizzBuzz".'''
for i in range(1,51):
    if i%3==0 and i%5==0:
        print(f"{i} : FizzBuzz")
    elif i%3==0:
        print(f"{i} : Fizz")
    elif i%5==0:
        print(f"{i} : Buzz")
    else:
        print(i,":")
  