'''Write a Python program to create a dictionary of Hindi words with their English
translations. Extend the program to allow the user to look up the English translation of a
Hindi word.'''

dictionary = {
    "नमस्ते": "Hello",
    "पुस्तक": "Book",
    "जल": "Water",
    "भोजन": "Food",
    "घर": "Home"
}
word = input("Enter a Hindi word: ")
if word in dictionary:
    print(f"The English translation is: {dictionary[word]}")
else:
    print("Word not found in the dictionary.")
