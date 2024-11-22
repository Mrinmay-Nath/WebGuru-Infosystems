a=input("Enter the string : ")
count={}
for i in a:
    if i in count:
        count[i] += 1
    else:
        count[i] =1
print(count)