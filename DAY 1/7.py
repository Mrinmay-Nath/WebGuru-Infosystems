a = input("Enter string: ")
b = a.lower()
count = 0
for z in b:
    if z == 'a' or z == 'e' or z == 'i' or z == 'o' or z == 'u':
        count += 1
print(f"No of vowels is {count}")