'''Given a list of names: ['Alice', 'Bob', 'Charlie', 'Diana'], write a program that uses
enumerate to print each name along with its position in the list.Also start the index from 1
instead of 0.'''

names=['Alice', 'Bob', 'Charlie', 'Diana']
for i, name in enumerate(names, start=1):
    print(f"{name} is at position {i}")