#Looping through a string
for x in "Collins Oduor":
    print(x)

#Determining the position of a char
x = 'Collins Oduor'
print(x[0], x[8], x[12])

#To determine if a word is present in a string (`in` is used) returns true if the word is present
x = "I am learning python"
if 'python' in x:
    print("Python is present")
#`not in` is used to reverse the effect of `in` i.e by returning true if the word is absent
x = 'Glad to have learnt C programming'
if 'python' not in x:
    print("Python is absent")
else:
    print('Python is present')