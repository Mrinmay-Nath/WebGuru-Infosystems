'''Create a Python program that greets the user based on the time of day. Use the “time”
module to get the current hour and offer greetings for Morning, Afternoon, and Evening.'''

import time
from datetime import datetime

def greet_user(name: str = "User") -> None:
    current_hour = datetime.now().hour
    if current_hour < 12:
        print(f"Good morning, {name}!")
    elif current_hour < 18:
        print(f"Good afternoon, {name}!")
    else:
        print(f"Good evening, {name}!")

def main() -> None:
    greet_user(input("Please enter your name: "))

if __name__ == "__main__":
    main()
    