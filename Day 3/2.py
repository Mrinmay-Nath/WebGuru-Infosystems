'''Design a Python program that runs a quiz game similar to "Kaun Banega Crorepati
(KBC)." Use a list of dictionaries to store each question along with four options, the
correct answer, and a prize for each question. Display the total prize money won at the
end.'''

print("Welcome to the Quiz Game! 🎮")
print("Rules:")
print("1. Answer each question by entering the number (1-4)")
print("2. Each correct answer wins you prize money!")
print("3. If you give a wrong answer, the game ends\n")
print("--------------------------------------------------------")
print("Let's begin! Good luck! 🍀\n")

questions = [
    "What is the correct file extension for Python files?",
    "Which keyword is used to define a function in Python?",
    "What is the output of 2 + 3 * 4 in Python?",
    "Which of these is a valid variable name in Python?",
    "Which data type is used to store text in Python?"
]
options = [
    ["1. .java", "2. .py", "3. .html", "4. .txt"],
    ["1. def", "2. func", "3. define", "4. function"],
    ["1. 20", "2. 14", "3. 12", "4. 10"],
    ["1. 2variable", "2. variable-2", "3. _variable", "4. variable name"],
    ["1. int", "2. str", "3. bool", "4. list"]
]
answers = [2, 1, 1, 3, 2]
prizes = [1000, 2000, 5000, 8000, 10000]
total_money = 0

for question_number in range(5):
    print(questions[question_number])
    print() 
    for option in options[question_number]:
        print(option)
    
    print("\nWhat's your answer?")
    while True:
        try:
            
            answer = int(input("Type 1, 2, 3, or 4: "))
            if answer >= 1 and answer <= 4:
                break  
            else:
                print("Please enter 1, 2, 3, or 4 only!")
        except:
            print("Please enter a number!")
    
    
    if answer == answers[question_number]:
        
        money_won = prizes[question_number]
        total_money = total_money + money_won
        print("\n🎉 Correct! You won ₹", money_won)
        print("Your total money now: ₹", total_money)
    else:
       
        print("\n❌ Sorry, that's not correct!")
        print("The right answer was:", answers[question_number])
        break  

